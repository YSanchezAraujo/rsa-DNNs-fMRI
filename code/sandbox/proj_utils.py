from PIL import Image
from torchvision import transforms
import torch

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
    pill_img = Image.open(img_path)
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225])
    ])
    if unsqueeze:
        return torch.unsqueeze(transform(pill_img), 0)
    return transform(pill_img)


class AlxLayerAct(torch.nn.Module):
    def __init__(self, net_num, orig_model):
        super(AlxLayerAct, self).__init__()
        self.features = torch.nn.Sequential(
            *list(orig_model.features.children())[:net_num]
        )
    def forward(self, x):
        x = self.features(x)
        return x
            
def get_layer_activation(data: torch.tensor, alexnet_model: torch.nn.Module, layer: int) -> torch.tensor:
    """
    parameters:
        data::torch.tensor - input data of the image, already
        processed with procces_img function
        
        alexnet_model::torch.nn.Module - pretrained alexnet model 
        loaded from torchvision
        
        layer::int - integer corresponding to the ReLU activation up 
        to a particular pare of the network
        
    returns:
        activations::torch.tensor - activation of the network up 
        until the ReLu of layer number: <layer>
    """
    mapper = {1:-12, 4:-9, 7:-6, 9:-4, 11:-2}
    if layer not in mapper.keys():
        raise Exception("layer must be one of: [1, 4, 7, 9, 11]")
    layer_model = AlxLayerAct(mapper[layer], alexnet_model)
    return layer_model(data)
