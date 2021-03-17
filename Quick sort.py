def QuickSort(A,start,end):
    if start<end:
        PIndex=Partition(A,start,end)
        QuickSort(A,start,PIndex-1)
        QuickSort(A,PIndex+1,end)
def Partition(A,start,end):
    PIndex= start
    pivot=A[end]
    for i in range(start,end):
        if A[i]<=pivot:
            A[i],A[PIndex]=A[PIndex],A[i]
            PIndex +=1
    A[PIndex],A[end]=A[end],A[PIndex]
    return PIndex
nums= [ 2, 3, 1, 5,20]
start=0
end = len(nums)-1
QuickSort(nums,start,end)
print(nums)