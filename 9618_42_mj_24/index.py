# binaryArray  = [1,2,3,4,5,6,7,8,9,10]

# def binarySearch(arr, low, high, x):
#     if high >= low:
#         mid = (low + high)//2

#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, low, mid-1, x)
#         else:
#             return binarySearch(arr, mid+1, high, x)
  

            
# x = binarySearch(binaryArray, 0, len(binaryArray)-1, 8)

# if x == -1:
#     print("not found")
# else:
#     print("found at index",x)


# def Power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * Power(x, n-1)

# product = 1
# def Power(x,n):
#     global product
#     while n != 0:
#         product = product * x
#         n = n-1
#     return product

# y = Power(2,10)
# print(y)

array = [1,2,3,4,5,6,7,8,9,10]

# def linearSearch(arr,x):
#     for i in range(0,len(arr)):
#         if arr[i] ==x:
#             return i
#     return -1
    
# x = linearSearch(array,12)

# if x == -1:
#     print("not found")
# else:
#     print("found at index",x)


def binarySearch(arr ,x):
    low = 0 
    high = len(arr)-1
    while high>= low:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binarySearchRecursive(arr,low , high,x):
    if high>=low:
        mid = (low + high) //2
        if arr[mid] ==x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr,low,mid-1, x)
        else: 
            return binarySearchRecursive(arr,mid+1,high, x)
    return -1



x = [10 ,11 ,5 ,1 ,20 ,7]
def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertionSort(arr):
    for  i in range(1,len(arr)):
        index = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > index:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = index
    return arr

# y = bubbleSort(x)
# print(y)

z = insertionSort(x)
print(z)