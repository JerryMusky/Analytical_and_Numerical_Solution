# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:31:26 2021

@author: Pei Ren
"""

#part 1

# import math as math
# import matplotlib.pyplot as plt

# x=0
# iter=0
# yanalyze=[]
# ycomp=[]

# stp1=0.1
# stp2=0.05


# def qn4P1(x):
#     y=math.sqrt(2/(1+2*math.exp(-10*x)))
#     return y

# def dxdyp1(y):
#     dxdy=5*y-5/2*y**3
#     return dxdy

# def step1(y,dxdy,step):
#     stp=y+step*dxdy
#     return stp

# while (x<50):
#     y=qn4P1(x)
#     dxdy=dxdyp1(y)
#     stp=step1(y,dxdy,stp1) #please change stp2 for 0.05 stepsize
#     yanalyze=yanalyze+[y]
#     ycomp=ycomp+[stp]
#     x=x+stp1 #please change stp2 for 0.05 stepsize
#     iter=iter+1

# print(iter)
# print(y,stp)

# plt.plot(yanalyze,'b')
# plt.plot(ycomp,'r')
# plt.legend(['Analytical solution','Numerical solution'])
# ax=plt.gca()


#part 2

# import math as math
# import matplotlib.pyplot as plt
# import numpy as np

# x=1
# iter=0
# yanalyze=[]
# ycomp=[]

# stp1=0.1
# stp2=0.05

# def qn4P2Root1(x):
#     y= x - math.sqrt(x**2 - 2*np.log(x))
#     return y

# def dxdyp2(y):
#     dxdy= (-(x*y) + 1) / (x**2 - x*y)
#     return dxdy

# def qn4P2Root2(x):
#     y=x+math.sqrt(x**2-2*np.log(x))
#     return y

# def stepfunc(y,dxdy,step):
#     stp=y+step*dxdy
#     return stp


# while (x<50):
#     y=qn4P2Root1(x) #please change to qn4P2Root2(x) for 2nd root
#     dxdy=dxdyp2(y)
#     stp=stepfunc(y,dxdy,stp1) #please change stp2 for 0.05 stepsize
#     yanalyze=yanalyze+[y]
#     ycomp=ycomp+[stp]
#     x=x+stp1 #please change to stp2 for 0.05 stepsize
#     iter=iter+1
    
# print('number of iterations is ',iter)    
# print(y,stp)


# plt.plot(yanalyze,'b')
# plt.plot(ycomp,'r')
# plt.legend(['Analytical solution','Numerical solution'])
# ax=plt.gca()
