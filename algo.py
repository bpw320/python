

def swap(A,i,j):
    s=A[i]
    A[i]=A[j]
    A[j]=s


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
              
def mergesort(A):
    mergesorthelper(A,0,len(A)-1) 

def mergesorthelper(A,i,j):
    
    if (j==i or j-i==1): #done
        if (j-i==1 and A[i]>A[j]):
           s=A[i]
           A[i]=A[j]
           A[j]=s
        return 
    rmid =  int((j-i+1)/2)
   
    mergesorthelper(A,i,i+rmid)
    mergesorthelper(A,i+rmid+1,j)
    merge(A,i,i+rmid,j)


def merge(A,i,imid,j):
    
    #A[i,imid]  sorted A[imid+1,j] sorted 
    B=list()
    k1=i
    k2=imid+1
    
    while k1<imid+1 and k2<=j:
        
        if (A[k1]<=A[k2]):
            B.append(A[k1])
            k1+=1
        else:
            B.append(A[k2])
            k2+=1
     #append remaining k2 ==j+1  k1=imid+1
     
    #if (k1==imid and k2>imid+1) or (k1==imid+1) or k2==imid+1:
    if  (k1==imid+1 or k2==imid+1 ):
        for k3 in range(k2,j+1):
            B.append(A[k3])
    if (k2==j+1 or k1==i ):
        for k3 in range(k1,imid+1):
            B.append(A[k3])
    t=0
    for k in range(i,j+1):
         A[k]=B[t]
         t+=1
       



def buildheap(A): #max-heap
    last = len(A)-1
    
    if last % 2  == 0:
        parent= int(last/2)-1
    else:
        parent = int(last/2)
    while parent>=0:
        heapify(A,parent)
        parent -= 1


def heapify(A,i): #for array A at i does not meet heap property
    left = 2*i+1 # Array starts with 0
    right = left+1
    if left>=len(A):
        return
    k=left

    if right<len(A) and A[left]<A[right]:
        k=right

    if A[i]<A[k]:
        swap(A,i,k)
        heapify(A,k)

    


def heapify1(A,i,end): #for array A at i does not meet heap property
    left = 2*i+1 # Array starts with 0
    right = left+1
    if left>=end:
        return
    k=left
    if right<end and A[left]<A[right]:
        k=right
    if A[i]<A[k]:
        swap(A,i,k)
    heapify1(A,k,end)


def heapsort(A):
    last= len(A)-1
    buildheap(A)
    while last>0:
        swap(A,0,last)
        heapify1(A,0,last)
        last -=1



import random
import datetime
import matplotlib.pyplot as plt
import numpy as npcls


A=list()
N=1000

for i in range(0,N):
  A.append(int(random.random()*10000) )


print(datetime.datetime.now())
#insertionsort(A)
#mergesort(A)
heapsort(A)

print(datetime.datetime.now())
#print(A)
#j=-1

#isheap=True
#for j in range(0,N):
#    l=2*j+1
#    r=l+1
#    if l>N-1:
        
#        break
#    if r>N-1:
#        break

    #if not A[j]>=A[l]:
    #    isheap=False
    #    print(j)
    #if not A[j]>=A[r]:
    #     isheap=False
    #     print(j)
  


j=-1
for i in range(0,N):
    
    if (j<=A[i]):
        j=A[i]
    else:
        print("wrong:",i,j,A[i])
    




#plt.scatter(x=range(0,N),y=A)
#plt.xticks(range(0,N))
#plt.show()

