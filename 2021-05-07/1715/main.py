import heapq

heap = []
for i in range(int(input())):
    heapq.heappush(heap, int(input()))

result = 0
for i in range(1, len(heap)):
    answer = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, answer)
    result += answer
print(result)
