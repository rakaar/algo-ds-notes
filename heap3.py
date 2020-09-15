# python supports for min heap only
# for max heap u need to multiply by -1

# there are some undocumented methods though :  _heapify_max, _heappop_pop

# suitable when u want to have a items sorted even if new elements keep on adding
# because when new elements keep on adding, u have to sort the array nlogn or even if u do binary search u wil have to do too many swaps(worst case of new element being 1st in the newly sorted array)
# with heaps it is easy(u will have to append to the list(constant time due to table doubling) and heapify parent of the appended child, logn operations max)
import heapq

q = [3,1,2]

heapq.heapify(q)

heapq.heappush(q, 4)
heapq.heappush(q, 18)
heapq.heappush(q, 120)
heapq.heappush(q, -1)
print(q)

heapq.heappop(q)
print(q)


print(heapq.nsmallest(3,q))
print(heapq.nlargest(3,q))

