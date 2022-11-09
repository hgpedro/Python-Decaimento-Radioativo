from random import random
import matplotlib.pyplot as plt
import numpy as np

N = 1000
lambd = 0.3
t = 0

listT = []
listN = []
LnN = []
ln = np.log(N)
LnN.append(ln)
listN.append(N)
listT.append(t)


while N > 1:
    decay = 0
    for i in range(N):
        if random() < lambd:
            decay += 1
    t += 1
    N = N - decay
    listN.append(N)
    listT.append(t)
    ln = np.log(N)
    LnN.append(ln)

plt.plot(listT,LnN)
plt.show()

plt.plot(listT,listN)
plt.show()
