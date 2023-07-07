#%%
import numpy as np
from numpy import linalg as LA

#Given the (3-2-1) Euler angle set with:
theta_1=20*np.pi/180 #radians
theta_2=10*np.pi/180 #radians
theta_3=-10*np.pi/180 #radians

#What is the equivalent (3-1-3) euler angle set????

#first let's calculate the corresponding rotation matrix for the (3-2-1) sequence
#C[θ1,θ2,θ3]=[M1(θ3)][M2(θ2)][M3(θ1)] (Forward mapping)

M1=np.array([[1,          0,              0       ],
             [0,  np.cos(theta_3), np.sin(theta_3)],
             [0, -np.sin(theta_3), np.cos(theta_3)]])

M2=np.array([[np.cos(theta_2),          0,   -np.sin(theta_2)],
             [      0,                  1,           0       ],
             [np.sin(theta_2),          0,    np.cos(theta_2)]])

M3=np.array([[ np.cos(theta_1), np.sin(theta_1),  0],
             [-np.sin(theta_1), np.cos(theta_1),  0],
             [         0,              0,         1]])

C=np.matmul(np.matmul(M1,M2),M3)


#Now for the (3-1-3) rotation sequence:
#R[α1,α2,α3]= [M3(α3)][M2(α2)][M3(α1)]
#the inverse mapping back to euler angles:

alpha_1=np.arctan2(C[2,0],-C[2,1])
alpha_2=np.arccos(C[2,2])
alpha_3=np.arctan2(C[0,2],C[1,2])

#print(alpha_1)
#print(alpha_2)
#print(alpha_3)


#############################################################
#Given the (3-2-1) Euler angle set with:
theta_1=10*np.pi/180 #radians
theta_2=20*np.pi/180 #radians
theta_3=30*np.pi/180 #radians



#first let's calculate the corresponding rotation matrix for the (3-2-1) sequence
#C[θ1,θ2,θ3]=[M1(θ3)][M2(θ2)][M3(θ1)] (Forward mapping)

M1=np.array([[1,          0,              0       ],
             [0,  np.cos(theta_3), np.sin(theta_3)],
             [0, -np.sin(theta_3), np.cos(theta_3)]])

M2=np.array([[np.cos(theta_2),          0,   -np.sin(theta_2)],
             [      0,                  1,           0       ],
             [np.sin(theta_2),          0,    np.cos(theta_2)]])

M3=np.array([[ np.cos(theta_1), np.sin(theta_1),  0],
             [-np.sin(theta_1), np.cos(theta_1),  0],
             [         0,              0,         1]])


#B frame relative to N
BN=np.matmul(np.matmul(M1,M2),M3)


#Now for the (3-1-3) rotation sequence:
#R[α1,α2,α3]= [M3(α3)][M2(α2)][M3(α1)]
#the inverse mapping back to euler angles:

#What is the equivalent (3-1-3) euler angle set????
alpha_1=np.arctan2(BN[2,0],-BN[2,1])
alpha_2=np.arccos(BN[2,2])
alpha_3=np.arctan2(BN[0,2],BN[1,2])

#print(alpha_1*180/np.pi)
#print(alpha_2*180/np.pi)
#print(alpha_3*180/np.pi)
#
###################################################################################
###################################################################################
#Given the (3-2-1) Euler angle set with:
theta_1=-5*np.pi/180 #radians
theta_2=5*np.pi/180 #radians
theta_3=5*np.pi/180 #radians



#first let's calculate the corresponding rotation matrix for the (3-2-1) sequence
#C[θ1,θ2,θ3]=[M1(θ3)][M2(θ2)][M3(θ1)] (Forward mapping)

M1=np.array([[1,          0,              0       ],
             [0,  np.cos(theta_3), np.sin(theta_3)],
             [0, -np.sin(theta_3), np.cos(theta_3)]])

M2=np.array([[np.cos(theta_2),          0,   -np.sin(theta_2)],
             [      0,                  1,           0       ],
             [np.sin(theta_2),          0,    np.cos(theta_2)]])

M3=np.array([[ np.cos(theta_1), np.sin(theta_1),  0],
             [-np.sin(theta_1), np.cos(theta_1),  0],
             [         0,              0,         1]])


#R frame relative to N
RN=np.matmul(np.matmul(M1,M2),M3)



###################################################################################
###################################################################################

#All the following Euler angle sets are 3-2-1 angles. The B frame
#relative to N is given through the 3-2-1 EAs (10,20,30) degrees, while
#R relative to N is given by the EAs (-5,5,5) degrees. 
#What is the attitude of B relative to R in terms of the 3-2-1 EAs


#Now attitude of B relative to R frame in terms of the 3-2-1 EAs:

BR=np.matmul(BN,np.transpose(RN))

#print("*****************")
#What is the equivalent (3-2-1) euler angle set????
alpha_1=np.arctan2(BR[0,1],BR[0,0])
alpha_2=-np.arcsin(BR[0,2])
alpha_3=np.arctan2(BR[1,2],BR[2,2])

print(alpha_1*180/np.pi)
print(alpha_2*180/np.pi)
print(alpha_3*180/np.pi)




# %%
 