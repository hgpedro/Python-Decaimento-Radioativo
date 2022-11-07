from random import random
from numpy import arange 
import matplotlib.pyplot as plt
import sympy

N = 1000
tau = 3.053*60
passo = 1
p = 1 - sympy.E**(-passo/tau)
tmax = 1000
DeltaT = arange(0,tmax, passo)
DeltaN = []

for t in DeltaT:
    DeltaN.append(N)
    decay = 0
    for i in range(N):
        if random()<p:
            decay += 1
    N -= decay

plt.plot(DeltaT,DeltaN)
plt.show()