from argparse import ArgumentParser
import nibabel as nib
import numpy as np
import os 
from brainiak.searchlight.searchlight import Searchlight
from scipy.stats import pearsonr
import numpy.ma as ma


def nnpart_files(part: int, paths: list) -> list:
    """
    DOC: TODO:

    """
    if part == 1:
        files = [x for x in paths if "p1fc" in x]
    elif part == 2:
        files = [x for x in paths if "p2fc" in x]

    return files


def rsa(data: np.array, mask: np.array, sl_rad: float, bcvar: np.array): 
    data4D = data[0]
    bolddata_sl = data4D[mask.astype(bool), :].T  
    human = np.corrcoef(bolddata_sl)
    alexnet = bcvar
    hvec = human[np.triu(np.ones(human.shape), k=10).astype(bool)]
    avec = alexnet[np.triu(np.ones(alexnet.shape), k=10).astype(bool)]
    # masking to ignore infs or nans, i.e. non-brain locations
    hvec_mask = ma.masked_invalid(hvec).mask
    if len(hvec[~hvec_mask]) == 0:
        return 0.0
    return pearsonr(hvec[~hvec_mask], avec[~hvec_mask])[0]


def run_anal(mask_path: str,
	     bold_path: str,
	     sl_rad: float, 
	     max_blk_edge: int, 
	     pool_size: int, 
	     nn_paths: list, 
	     part: int,
	     save_dir: str,
	     rsa) -> bool:
    """
    DOCS: TODO:
 
    """
    # extract the subject string from the bold path
    sub = bold_path.split("/")[-1].split(".")[0].split("_")[-1]
    print("starting run {}".format(sub))

    # this is to account for if we're using part 1 of the movie clip or part 2
    if part == 1:
        tr_start_idx = 0
        tr_end_idx = 946
    elif part == 2:
        tr_start_idx = 946
        tr_end_idx = 1976

    # get the correct correlation matrices for alexnet
    nncor_files = nnpart_files(part, nn_paths)

    # nibabel load, this loads an object but not the numpy arrays of the data
    mask_obj = nib.load(mask_path)
    bold_obj = nib.load(bold_path)
    
    # converting to numpy arrays
    data = np.array(bold_obj.dataobj)[:, :, :, tr_start_idx:tr_end_idx]
    mask = np.array(mask_obj.dataobj).astype(int)

    sl = Searchlight(sl_rad = sl_rad, max_blk_edge = max_blk_edge)
    sl.distribute([data], mask)

    counter = 0
    for nn_path in nncor_files:
        # this is alexnet
        bcvar = np.load(nn_path)
        save_name = nn_path.split("/")[-1].split(".")[0]
	
	# broadcast the NN matrix
        sl.broadcast(bcvar)

        # now the rsa part
        sl_result = sl.run_searchlight(rsa, pool_size=pool_size)
        sl_result[sl_result == None] = 0
        sl_data = np.array(sl_result, dtype=float)
        sl_img = nib.Nifti1Image(sl_data, affine=mask_obj.affine)

        # save the result to file as a nifti image
        save_path = os.path.join(save_dir, save_name + "_" + sub)
        sl_img.to_filename(save_path + ".nii.gz")
        
        counter += 1

    if counter == len(nncor_files):
        print("\nCOMPLETE SUCCESSFULLY\n")
        return True

    print("\nSOMETHING FAILED\n")
    return False
    

def main():
    DATA_DIR = "/scratch/sherlock_neu502b/data/movie_files"
    FILES = [os.path.join(DATA_DIR, x) for x in os.listdir(DATA_DIR) if x.endswith(".nii")]
    MASK_PATH = "/scratch/sherlock_neu502b/data/derivatives/3mm_mask.nii.gz"
    NNCOR_DIR = "/scratch/sherlock_neu502b/results/nncormats"
    #NNCOR_FILES = [os.path.join(NNCOR_DIR, x) for x in os.listdir(NNCOR_DIR) if x.endswith(".npy")]
    NNCOR_FILES = [os.path.join(NNCOR_DIR, x) for x in os.listdir(NNCOR_DIR) if "fc" in x]
    RES_DIR = "/scratch/sherlock_neu502b/results/rsak10fc"
   
    # get arguments from argparser
    BOLD_PATH = args.bold_path
    SL_RAD = args.sl_rad
    MAX_BLK_EDGE = args.max_blk_edge
    POOL_SIZE = args.pool_size

    # left over runs
    #ld = {
    #        6:[1, 9, 11],
    #	    7:[9, 11], 
    #        8:[1, 9, 11],
    #        9:[9, 11],
    #        10:[9, 11],
    #        11:[9, 11],
    #        12:[9, 11],
    #        13:[9, 11],
    #        14:[9, 11],
    #        15:[1, 4, 9, 11],
    #        16:[1, 9, 11],
    #        17:[9, 11]
    #}

    #f = lambda x: x.split("relu")[-1].split("cormat")[0]
    #sub_num = int(BOLD_PATH.split("_")[-1].split(".")[0].split("s")[-1])
    #nn_sub_files = [x for x in NNCOR_FILES if int(f(x)) in ld[sub_num]]

    # run rsa analyses for parts 1 and 2
    for part in [1, 2]:
        run_anal(MASK_PATH, 
		 BOLD_PATH, 
		 SL_RAD, 
		 MAX_BLK_EDGE, 
		 POOL_SIZE, 
		 NNCOR_FILES, 
		 part,
		 RES_DIR,
		 rsa)    


if __name__ == "__main__":
    parser = ArgumentParser(prog="batch.py", description=__doc__)
    parser.add_argument("-bp", "--bold_path", type=str, help="participant bold path")
    parser.add_argument("-slrad", "--sl_rad", type=int, help="search light radius")
    parser.add_argument("-mbe", "--max_blk_edge", type=int, help="max block edge")
    parser.add_argument("-pl", "--pool_size", type=int, help="pool size")
    args = parser.parse_args()
    
    main()

