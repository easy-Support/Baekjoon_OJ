import sys

repair_count, tape_length = map(int, sys.stdin.readline().split())
repair_list = list(map(int, sys.stdin.readline().split()))
repair_list.sort()

answer = 1
last = repair_list[0] + tape_length - 1

for tape in repair_list:
    if last < tape:
        last = tape + tape_length - 1
        answer += 1
print(answer)
