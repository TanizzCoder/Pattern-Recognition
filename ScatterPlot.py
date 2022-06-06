import numpy as np
import matplotlib.pyplot as plt
import random
n=int(input("Enter the value of n: "))
l=[]
a=[]
for i in range(0,n):
    for j in range(0,2):
        l.append(random.random())
    a.append(l)
m=np.array(a)
plt.title("SCATTER PLOT")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
for i in range(0,n):
    for j in range(0,2):
        plt.scatter(m[i],m[j])
plt.show()
