#%%
import numpy as np
from numpy import linalg as LA

#Let the [BN] direction cosine matrix (DCM) be given by:
BN=np.array([[-0.87097,  0.45161, 0.19355],
             [-0.19355, -0.67742, 0.70968],
             [ 0.45161,  0.58065, 0.67742] ])
print("BN:")
print(BN)
#Let the anguar velocity vector be:(the rotation rate of a rigid body is express
#through the body angular velocity vector)
w1=0.1
w2=0.2
w3=0.3
w_BN=np.array([w1, w2, w3])
#this vector determines how a body will rotate, and thus how the DCM
#describing the orientation will evolve. 
# This vector must be taken with respect to the B coordinate frame
print("Omega BN")
print(w_BN)
#Omega tilde is
w_tilde_BN=np.array([[ 0, -w3,  w2],
                     [ w3,  0, -w1],
                     [-w2, w1,  0]])

#Now the corresponding DCM rates is:
BN_dot=-1*np.matmul(w_tilde_BN,BN)
print("BN_dot:")
print(BN_dot)








# %%
