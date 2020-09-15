from collections import Counter
import time
import random

with open('b.txt') as f:
    x = f.read()

words = x.split(' ')



start = time.time()
### lib ###
# count = Counter(words)

## Personal ###
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(time.time() - start)

print(count)


