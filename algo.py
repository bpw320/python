
def insertionsort(A):
    l=len(A)
    k=1
    while k<l:
        #0..k-1 sorted 
        #find position to insert A[k]  A[k]=A[k-1]
        i=k
        s=A[k]
        ismoved=0
        for i in range(k-1,-1,-1):
            if (s>=A[i]):
                break
            else:
                ismoved=1
                A[i+1]=A[i]
        if ismoved:
            A[i]=s
        
        k +=1
              

import random
import datetime
import matplotlib.pyplot as plt
import numpy as np

A=list()
N=1000000
for i in range(0,N):
  A.append(int(random.random()*1000) )
print(A)

print(datetime.datetime.now())
insertionsort(A)
print(datetime.datetime.now())

print(A)

plt.scatter(x=range(0,N),y=A)
plt.show()

