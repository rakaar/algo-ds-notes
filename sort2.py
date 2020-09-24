# counting sort
# let n = 10, number of elements to be sorted
# k = 5 , the maximum integer
n = 10
k = 5
counter = [0 for i in range(k+1)]
arr = [4,5,2,3,4,1,2,1,4,3]
def counting_sort():
    for i in range(len(arr)):
        counter[arr[i]] += 1
    sorted_arr = []
    for i in range(len(counter)):
        num_of_times = counter[i]
        for _ in range(num_of_times):
            sorted_arr.append(i)
        # below is using an extra array, which is bad bcoz of extra space
        # writing in above way also helps to avoid an extra if checking
        # though loops in loops look bad, sometimes they are needed
        # if num_of_times != 0:
        #     mini_arr = [i for k in range(num_of_times)]
        #     sorted_arr.extend(mini_arr)
    
    print('sorted array is ',sorted_arr)


counting_sort()

# items which are repeated to be in the same order as their input
# called as "Stable"

n = 10
k = 5
counter = [[] for i in range(k+1)] # O(k)
arr = [4,5,2,3,4,1,2,1,4,3]
def stable_counting_sort():
    for i in arr: # n times            | these 2 lines would take 
        counter[i].append(i) # O(1)    |  O(n)
    sorted_arr = []
    for a in counter:        # k times
        if len(a) == 0:      #                 |    sigma(Li) + sigma(1) = n + k
            continue         #                 | i:1->k          i:1->k   
        sorted_arr.extend(a) #  O(Li + 1)
 
    print('sorted array is ',sorted_arr) 

stable_counting_sort()
# ex - 1
n = 5
k = 4
counter = [0 for i in range(k+1)] # O(k)
arr = [4,1,3,4,3]

# ex - 2
n = 10
k = 5
counter = [0 for i in range(k+1)]
arr = [4,5,2,3,4,1,2,1,4,3]

#  a 0->1 1->3 2->3 3->4 4->4
#  c 0->0 1->1 2->0 3->2 4->2
#  c'0->0 1->1 2->1 3->3 4->5
def stable_counting_sort2():
    for i in range(len(arr)): # O(n)
        counter[arr[i]] += 1
    v = 0
    for i in range(len(counter)): # O(k)
        if i == 0:
            v += counter[i]
            continue
        v += counter[i]
        counter[i] = v
    sorted_arr = [0 for i in range(n)] #O(n)
    for i in range(len(arr)-1,-1,-1):  #O(n)
        number = arr[i]
        pos = counter[number] - 1
        sorted_arr[pos] = number
        counter[number] -= 1
    print('sorted array is ',sorted_arr)  # overal its O(n+k)
        
stable_counting_sort2()

# radix sort for base 10, 4 digits

def count_sort4radix(arr, pos):
    # hard_coding 
    n = 7
    k = 4
    counter = [0 for i in range(k+1)]
    digs_arr = [int(str(i)[pos]) for i in arr]
    for i in range(len(digs_arr)): # O(n)
        counter[digs_arr[i]] += 1
    v = 0
    for i in range(len(counter)): # O(k)
        if i == 0:
            v += counter[i]
            continue
        v += counter[i]
        counter[i] = v
    sorted_arr = [0 for i in range(n)] #O(n)
    for i in range(len(arr)-1,-1,-1):  #O(n)
        actual_number = arr[i]
        number = digs_arr[i]
        pos = counter[number] - 1
        sorted_arr[pos] = actual_number
        counter[number] -= 1
    return sorted_arr


def radix_sort():
    nums = [2341, 1432, 2413, 1243, 2143, 1234, 1423]
    for i in range(3,-1,-1):
        nums = count_sort4radix(nums, i)
    print('radix ',nums)    

radix_sort()