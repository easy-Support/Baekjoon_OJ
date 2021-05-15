import sys
import heapq

jewellery_count, bag_count = map(int, sys.stdin.readline().split())

info = [list(map(int, sys.stdin.readline().split())) for _ in range(jewellery_count)]
bag = [int(sys.stdin.readline()) for _ in range(bag_count)]

info.sort()
bag.sort()

temp = []

index = 0
answer = 0
for bag_weight in bag:
    while index < len(info) and bag_weight >= info[index][0]:
        heapq.heappush(temp, -info[index][1])
        index += 1

    if temp:
        answer += heapq.heappop(temp)

print(-answer)
