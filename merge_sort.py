def merge_sort(arr):
    length = len(arr)
    if length == 1:
        print('recu end',arr)
        return arr
    mid = length//2
    
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged_arr = []
    # two finger algo
    left_ptr = left_half[0]
    right_ptr = right_half[0]

    # you should stop when one of them is empty, because when one is empty all u need to do is append the non empty one to the result
    while len(left_half) > 0 and len(right_half) > 0:
        if left_ptr <= right_ptr:
            num = left_half.pop(0)
            merged_arr.append(num)
            if len(left_half) > 0:
                left_ptr = left_half[0]
        elif right_ptr < left_ptr:
            num = right_half.pop(0)
            merged_arr.append(num)
            if len(right_half) > 0:
                right_ptr = right_half[0]

    if len(left_half) == 0:
        merged_arr.extend(right_half)
    else:
        merged_arr.extend(left_half) 

    print('merged-are ',merged_arr)
    return merged_arr     


print(merge_sort([5,2,4,6,1,3]))

## complexity - o  of log n times n - proof - intutively explained using recursion tree