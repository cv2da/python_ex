#%%
import numpy as np
from numpy import linalg as LA
#to run the interactive window you need the header comment to show the run cell option

A=np.array([[-6, 3],
             [4, 5]])
print("A:",A)

w,v=LA.eig(A)

print("w1:",w[0])#eigenvalues
print("w2:",w[0])
print("v1:",v[:,0])#normalized eigenvector
print("v2:",(1/v[0,1])*v[:,1])#not normalized eigenvector

# %%
