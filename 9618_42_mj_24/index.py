binaryArray  = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(low,high,x,arr):
    while low<=high:
        mid = (low+high)//2

        if arr[mid] ==2:
            return mid
        elif arr[mid] >x:
            return binarySearch[low,mid-1,x,arr]
        else:
            return binarySearch[low,mid+1,x,arr]
    return -1

            
x = binarySearch(0,len(binaryArray)-1,2,binaryArray)
print(x)