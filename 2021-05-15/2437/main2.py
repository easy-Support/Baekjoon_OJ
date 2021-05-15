import sys
from itertools import combinations

weight_length = int(input())
weight_list = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in range(weight_length):
    for weight_comb in combinations(weight_list, i):
        weight_sum = sum(weight_comb)
        dic[weight_sum] = True

answer = 1
nums = dic.keys()
while True:
    if answer in nums:
        answer += 1
    else:
        break
print(answer)
