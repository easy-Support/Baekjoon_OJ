import sys

index = 0
dic = {
    "0": [],
    "1": []
}

for num in sys.stdin.readline().strip():
    temp = [index]
    if len(dic[num]) != 0 and index == dic[num][-1][-1] + 1: # 연속된 수 일 경우 묶기
        temp = dic[num].pop()
        temp.append(index)
    dic[num].append(temp)
    index += 1

zero_length = len(dic["0"])
one_length = len(dic["1"])

answer = one_length if zero_length >= one_length else zero_length
print(answer)
