#%%
import numpy as np
from numpy import linalg as LA


BN=np.array([[-0.87097,  0.45161, 0.19355],
             [-0.19355, -0.67742, 0.70968],
             [ 0.45161,  0.58065, 0.67742] ])
print("BN:")
print(BN)

w,v=LA.eig(BN)

print("w:")
print(w)
print()
print("v1:",v[:,0])
print("v2:",v[:,1])
print("v3:",v[:,2])

# %%
