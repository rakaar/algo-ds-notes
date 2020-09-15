# heap with index zero

# this is not written in this way bcoz
#     # 1 - not all languages support negative index operation as it would return error in other cases
#     # 2 - here every time u have to check if right is -1 or not and it causes fuzy
# def max_heapify(arr, n, i):
#     left = 2*i if 2*i <= n else -1
#     right = 2*i + 1 if 2*i + 1 <= n-1 else -1
    
#     # if already max return
#     if left == -1:
#         return
#     elif (arr[i] >= arr[left]) and (right == -1 or arr[i] >= arr[right]):
#         return
    
#     if arr[left] > arr[i]:
#         arr[left], arr[i] = arr[i], arr[left]
#     elif right != -1 and arr[right] >


arr =  [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17 ]

print('before heaping ', arr)
# heap with index zero
def max_heapify(arr, n, i):
    left = 2*i + 1
    right = 2*i + 2

    # lets assume that largest the arr[i] is the max heap only
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # if our assumption that i index element is already max heap, swap and recurisvely call it
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_heap(arr, n):
    start = n//2 - 1
    for i in range(start, -1, -1):
        max_heapify(arr, n, i)    


build_heap(arr, len(arr))
print('arr ', arr)

sorted_arr = []
num_elements = len(arr)
for i in range(0, num_elements):
    sorted_arr.append(arr[0])
    length = len(arr)
    # if u plan to remove the largest number directly from the heap, u may have to rebuild it
    # instead swap with the last node,and then remove the last node
    # the reason that it works well is when u swap the root node is not a maxheap but its children are max heaps, hence u can run max_heapify on the root node
    arr[0],arr[length-1] = arr[length-1], arr[0]
    # to indciate swapping alternatively u could just assign
    #  arr[0] = arr[length-1] 
    arr.pop(length-1)
    # the good reason to use this max_heapify is that it works in logn time, due to the fact that its children(children of arr[0] are max heaps)
    max_heapify(arr, len(arr), 0)

print('sroted arr ',sorted_arr)