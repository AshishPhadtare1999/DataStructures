### Array Data Structures....
### Kadane's Algorithm VVV IMP.
def Kadanes(arr):
    maxsum=0
    cumsum=0
    for i in range(0,len(arr)):
        cumsum+=arr[i]
        if cumsum<0:
            cumsum=0
        if cumsum>maxsum:
            maxsum=cumsum
arr=[-2,-3,4,-1,-2,1,5,-3]
print(Kadanes(arr))