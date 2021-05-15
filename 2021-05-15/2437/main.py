import sys

input()
weight_list = list(map(int, sys.stdin.readline().split()))
weight_list.sort()

answer = 1
for i in weight_list:
    if answer >= i:
        answer += i
    else:
        break
print(answer)
