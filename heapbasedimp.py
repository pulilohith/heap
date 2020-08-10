import random
def heapify(arr,length,i):
    larg=i 
    left=2*i+1 
    right=left+1 
    if(left<length and arr[left]>arr[larg]):
        larg=left
    if(right<length and arr[right]>arr[larg]):
        larg=right
    if(larg!=i):
        arr[larg],arr[i]=arr[i],arr[larg]
        heapify(arr,length,larg)
def heapsort(arr):
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i)
    for j in range(len(arr)-1,-1,-1):
        arr[0],arr[j]=arr[j],arr[0]
        heapify(arr,j,0)
    print(arr) 
def heapsortiter(arr):
    for i in range(len(arr)-1,0,-1):
        if(arr[i]>arr[(i-1)//2]):
            j=i 
            while(j!=0 and arr[i]>arr[(j-1)//2]):
                arr[j],arr[(j-1)//2]=arr[(j-1)//2],arr[j]
                j=(j-1)//2  
    for j in range(len(arr)-1,-1,-1):
        arr[0],arr[j]=arr[j],arr[0]
        larg,i=0,0
        while(True):
            left=2*i+1 
            right=left+1 
            if(left<j and arr[left]>arr[larg]):
                larg=left
            if(right<j and arr[right]>arr[larg]):
                larg=right
            if(larg!=i):
                arr[larg],arr[i]=arr[i],arr[larg]
                i=larg
            else:
                break
    print(arr) 
def kthlargest(arr,k):
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i)
    for j in range(1,k):
        arr[0]=arr[len(arr)-j]
        heapify(arr,len(arr)-j,0)
    print(arr[0])
def Quickselect(arr,k):
    low=0
    high=len(arr)-1 
    while(low<high):
        rand=random.randint(low,high)
        f=partition(arr,low,high,rand)
        if(f==len(arr)-k):
            return arr[f]
        elif(f>(len(arr)-k)):
            right=f-1 
        else:
            left=f+1 
    return -1 
def partition(arr,low,high,k):
    pivot=arr[k]
    curen=low
    arr[high],arr[k]=arr[k],arr[high]
    while(low!=high):
        if(arr[low]<pivot):
            arr[curen],arr[low]=arr[low],arr[curen]
            curen+=1 
        low+=1 
    arr[curen],arr[high]=pivot,arr[curen]
    return curen
        
            
heapsort([54,32,12,4,21,46,42,98]) 
heapsortiter([54,32,12,4,21,46,42,98]) 
kthlargest([54,32,12,4,21,46,42,98],8-3+1) 
print(Quickselect([54,32,12,4,21,46,42,98],3))
