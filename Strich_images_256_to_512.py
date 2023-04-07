import numpy as np
from tifffile import imread
from tifffile import imsave
#input of the algorithm: prediction_test.tif
#output of the algorithm: Exp_1_P.tif
#the input file must be placed in the same folder as the .py file but this can be modified
stack_1 = imread("prediction_test.tif")

stack_ca_drehung = np.zeros(shape=(int(stack_1.shape[0]/4), 512, 512), dtype=np.uint32)

for i in range(int(stack_1.shape[0]/4)):
    stack_ca_drehung[i, 0:256, 0:256] = stack_1[i]
    stack_ca_drehung[i, 0:256, 256:512] = stack_1[i+int(stack_1.shape[0]/4)]
    stack_ca_drehung[i, 256:512, 0:256] = stack_1[i+2*int(stack_1.shape[0]/4)]
    stack_ca_drehung[i, 256:512, 256:512] = stack_1[i+3*int(stack_1.shape[0]/4)]   
    
    
imsave("Exp_1_P.tif", stack_ca_drehung.astype(np.uint32))