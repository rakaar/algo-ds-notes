arr = [5,2,4,6,1,3]

# insert sort
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    # the idea is to keep pushing the key inside the sorted array till it finds it proper place
    while j >=0 and arr[j] > key:
        arr[j], arr[j+1] = key, arr[j]
        j -= 1
        print(arr)


# optimised insertion
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    # the idea is to keep pushing the key inside the sorted array till it finds it proper place
    # but u can take advantage of the fact that u have to push the number inside a sorted array
    # so basically u look to insert at the middle, if fail then go to the left half or the right half accordingly
    # hence reducing half the places

    ## but the problem with inserting by binary search is that it requires shifting all the elements to the right,
    # which is an expensive job in sense that it again leads to n^2, because in worst u shift all the elements to right
    while j >=0 and arr[j] > key:
        arr[j], arr[j+1] = key, arr[j]
        j -= 1
        print(arr)
        
    
print(arr)