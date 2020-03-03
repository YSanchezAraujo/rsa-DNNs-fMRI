import torch
import torchvision.models as models
from pprint import pprint

# get the model
alexnet = models.alexnet()
# get a dictionary of all weight vectors in the model
states = alexnet.state_dict()
# look at the keys
pprint(states.keys())
# acces weights for a particular part of the model
states["features.0.weight"]

