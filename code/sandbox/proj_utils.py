from PIL import Image
from torchvision import transforms
import torch
import numpy as np

# FUCNTION BELOW NOT IN USE ANYMORE, TO BE DELETED 
def gen_batch(iterable: range, batch_size: int) -> iter:
    """
    parameters:
        iteratble::range - range object with the upper as
        the total number of frames
        
        batch_size::int - the step size for the range object,
        this will be used to creat batches of length <batch_size>
        
    returns:
        iterable::range - range object with at the current position
        along the total number of frames, of length <batch_size>
    """
    l = len(iterable)
    for ndx in range(0, l, batch_size):
        yield iterable[ndx:min(ndx + batch_size, l)]
        
        
def _mid_slice_idxs(max_len: int, can_use_range: tuple) -> tuple:
    """
    parameters:
        max_len::int - how big we are allowing the resulting list to be
        
        can_use_range::tuple - tuple of 2 ints, denoting the
        max of the range we can use and the min
        
    returns:
        ::range  with the start and end indices giving the middle
        <max_len> values of the collection it is applied to
    """
    diff = can_use_range[1] - can_use_range[0]
    mid = int(diff / 2)
    to_remove = diff - max_len
    if to_remove > 1:
        side_remove = int(to_remove / 2)
    else:
        side_remove = 0
    return range(int(can_use_range[0] + side_remove), int(can_use_range[1] - side_remove + 1))     


def gen_ranges(batch_size: float, tr_total: int, max_len: int) -> iter:
    """
    parameters:
        batch_size::float - the number of frames in a TR, roughly
        
        tr_total::int - total number of TRs acquired for the scans
        
        max_len::int - the length of the truncated number of trs that 
        we'll use to try and reduce TR to TR autocorrelation in the signal
        
    returns:
        ::iter - generates the ranges to be used for each TR, taking into
        account all of the input parameters
    """
    tr_counter = 0
    while tr_counter < tr_total:
        tr_counter += 1
        can_use_range = (int(tr_counter*batch_size) + 2, int((tr_counter+1)*batch_size) - 2)
        yield _mid_slice_idxs(max_len, can_use_range)

        
def sort_files(file_list: list) -> np.array:
    """
    parameters:
        file_list::list - paths for all pngs of the sherlock movie
    
    returns:
        sorted_file_list::np.array(type::strings) - sorted version of
        file_list, sorted by the frame number
    """
    sorted_list = []
    for i in file_list:
        sorted_list.append(int(i.split("_")[-1].split(".")[0]))
    return np.array(file_list)[np.argsort(sorted_list)]


def process_img(img_path: str, unsqueeze: bool = False) -> torch.tensor:
    """
    parameters:
        img_path::String - path to where the .png file lives on
        the filesystem
    
        unsqueeze::Bool - value dictating whether to add an extra dimension
        using torches unsqueeze function, at the start of the shape.
        example: (3,4) --> (1, 3, 4) if unsqueeze == True
    
    returns:
        a pytorch tensor of shapes:
            (3, 244, 244) or (1, 3, 244 244)
    """
    with Image.open(img_path) as pill_img:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean = [0.485, 0.456, 0.406],
                std = [0.229, 0.224, 0.225])
        ])
        if unsqueeze:
            return torch.unsqueeze(transform(pill_img), 0)
        return transform(pill_img)

# this one is for the conv layers
class AlxLayerAct(torch.nn.Module):
    def __init__(self, net_num, orig_model):
        super(AlxLayerAct, self).__init__()
        self.features = torch.nn.Sequential(
            *list(orig_model.features.children())[:net_num]
        )

    def forward(self, x):
        x = self.features(x)
        return x

    
def layer_acts(data: torch.tensor, alexnet_model: torch.nn.Module, layer: int) -> torch.tensor:
    """
    parameters:
        data::torch.tensor - input data of the image, already
        processed with procces_img function

        alexnet_model::torch.nn.Module - pretrained alexnet model 
        loaded from torchvision

        layer::int - integer corresponding to the ReLU activation up 
        to a particular pare of the network

    returns:
        activations::torch.tensor - forward pass of the network up 
        until layer number: <layer>
    """
    mapper = {1:-12, 4:-9, 7:-6, 9:-4, 11:-2}
    if layer not in mapper.keys():
        raise Exception("layer must be one of: [1, 4, 7, 9, 11]")
    layer_model = AlxLayerAct(mapper[layer], alexnet_model)
    return layer_model(data)


def all_acts(data: torch.tensor, alexnet_model: torch.nn.Module) -> dict:
    """
    parameters:
        data::torch.tensor - input data of the image, already
        processed with procces_img function
        
        alexnet_model::torch.nn.Module - pretrained alexnet model 
        loaded from torchvision
        
    returns:
        activations::dict(int:torch.tensor) - forward pass of the network up 
        until layer number: <layer>, for all relevant layers     
    """
    layers = (1, 4, 7, 9, 11)
    acts = {}
    for val in layers:
        acts[val] = layer_acts(data, alexnet_model, val)
    return acts
    
# this one is for the fully connected layers
class AlxLayerFcAct(torch.nn.Module):
    def __init__(self, net_num, orig_model):
        super(AlxLayerFcAct, self).__init__()
        self.features = torch.nn.Sequential(
            *list(orig_model.features.children())
        )
        
        self.avgpool = torch.nn.AdaptiveAvgPool2d(output_size=(6, 6))
        
        self.clf = torch.nn.Sequential(
            *list(orig_model.classifier.children())[:net_num]
        )
        
        
    def forward(self, x):
        return self.clf(
            torch.flatten(self.avgpool((self.features(x))), 1)
        )
    
def layer_acts_fc(data: torch.tensor, alexnet_model: torch.nn.Module, layer: int) -> torch.tensor:
    """
    parameters:
        data::torch.tensor - input data of the image, already
        processed with procces_img function
        
        alexnet_model::torch.nn.Module - pretrained alexnet model 
        loaded from torchvision
        
        layer::int - integer corresponding to the ReLU activation up 
        to a particular pare of the network
        
    returns:
        activations::torch.tensor - forward pass of the network up 
        until layer number: <layer>
    """
    mapper = {2:-5, 5:-2, 6:-1}
    if layer not in mapper.keys():
        raise Exception("layer must be one of: [2, 5, 6]")
    layer_model = AlxLayerFcAct(mapper[layer], alexnet_model)
    return layer_model(data)


def all_acts_fc(data: torch.tensor, alexnet_model: torch.nn.Module) -> dict:
    """
    parameters:
        data::torch.tensor - input data of the image, already
        processed with procces_img function
        
        alexnet_model::torch.nn.Module - pretrained alexnet model 
        loaded from torchvision
        
    returns:
        activations::dict(int:torch.tensor) - forward pass of the network up 
        until layer number: <layer>, for all relevant layers     
    """
    layers = (2, 5, 6)
    acts = {}
    for val in layers:
        acts[val] = layer_acts_fc(data, alexnet_model, val)
    return acts


def correlation_mat(data: np.array) -> np.array:
    """
    parameters:
        data::np.array - concatenated (by TR) layer activations
        
    returns:
        correlation_matrix::np.array - correlation matrix of the activations over TRs
    """
    X, Y, Z, T = data.shape
    coln = Y * Z * T
    data = data.reshape(X, coln)
    return np.corrcoef(data)


# def simple_group_stats(data_paths: list, p: int, binary: bool, nifti: bool, shape: tuple) -> nib.Nifti1Image:
#     """
#     for each subject, make a volume where a voxel is 1 if it was in the top 1% for
#     that subject/layer and 0 if it wasn’t (edited) 
#     this should give you 16 volumes per layer (because 16 subjects)
#     then sum across subjects so you get a volume per layer
#     and look how it changes
#     """
#     # to save layer specific images
#     result = np.zeros(shape)
    
#     #sn = lambda x: x.split("_")[-1].split(".")[0]
    
#     for dp in data_paths:
#         data_obj, data = load_rsa(dp)
#         result += toppvol(data, p=p, affine=data_obj.affine, binary=binary, nifti=nifti)
    
#     return nib.Nifti1Image(result, affine=data_obj.affine)