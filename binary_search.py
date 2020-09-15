arr = [1,2,3,4,5,6,7,8,9,10]
length = len(arr)

def binary_search(l, r, num):
    '''
    takes l r  returns index of num
    '''
    if l <= r:
        m = (l + r) // 2
        if arr[m] == num:
            return m
        elif arr[m] > num:
            return binary_search(0, m-1, num)
        else:
            return binary_search(m+1, length-1, num)
    else:
        return -1


print(binary_search(0, length-1, 100))