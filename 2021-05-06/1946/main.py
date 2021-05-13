import sys

a = [[list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))] for _ in range(int(input()))]

for i in a:
    i.sort(key=lambda x: x[0])
    count = 1
    m = i[0][1]
    for j in range(1, len(i)):
        if i[j][1] < m:
            count += 1
            m = i[j][1]
    print(count)
