arr =  [10, 20, 15, 2, 23, 90, 67]
# arr = [5, 10, 20, 15]
length = len(arr)
for i in range(length):
    if i == 0:
        if(arr[i+1] < arr[i]):
            print(arr[i])
    elif i == length-1:
        if(arr[i] > arr[i-1]):
            print(arr[i])
    else:
        if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            print(arr[i])
