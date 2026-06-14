#all import
# import recipes.flavours #folder.filename #fetching whole book

# print(recipes.flavours.elaichi_chai()) 

#named import
from recipes.flavours import elaichi_chai, masala_chai
print(elaichi_chai())

#relative import .
from .recipes.flavours import masala_chai

#avoid this 
from recipes import *

#__init__
# - empty file for python to understand this dir is a module.
# from v3.3 and + its obeslete by python