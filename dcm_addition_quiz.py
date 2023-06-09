#%%
import numpy as np
from numpy import linalg as LA


#Addition of DCM means multiply so we go from one frame of reference 
#to another

#Given three reference frame N, B, and F,
#let the unit base vectors of the coordinate frames B and F be:
#unit base vector components are written in the N frame
b1=(1/3)*np.array([1,2,-2])
b2=(1/np.sqrt(2))*np.array([0,1,1])
b3=(1/(3*np.sqrt(2)))*np.array([4,-1,1])

f1=(1/4)*np.array([3,-2,np.sqrt(3)])
f2=(1/2)*np.array([-1,0,np.sqrt(3)])
f3=(-1/4)*np.array([np.sqrt(3),2*np.sqrt(3),1])


BN=np.array([b1,b2,b3])
print("BN:")
print(BN)

FN=np.array([f1,f2,f3])
print("FN:")
print(FN)

#Determine the DCM [BF]?

#first calculate inverse(which is the same as transpose for DCM)
NF=FN.transpose()
print("NF:")
print(NF)

#now the SOLUTION:
BF=np.matmul(BN,NF)
print("BF:")
print(BF)


###########################################################################
#2)
#B is rotated 90 degrees about the first axis relative to N
#relative to N means that we already in the N frame: [NB]

NB=np.array([[1, 0,  0],
             [0, 0, -1],
             [0, 1,  0]])


#R is rotated -90 degrees about the second axis relative to N
#relative to N means that we already in the N frame: [NR]

NR=np.array([[0, 0, -1],
             [0, 1,  0],
             [1, 0,  0]])

#what is the [BR] DCM? SOLUTION:
print("*"*12)
BR=np.matmul(NB.transpose(),NR)
print("BR:")
print(BR)

# %%
