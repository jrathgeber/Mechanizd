# heaps

import heapq

# under the hood are arrays
minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 5)

# min is allways at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# no Max Heap !!

# under the hood are arrays
maxHeap = []

heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -5)

# get the max
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


# build a heap in linear time
arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))