def check(list_num):
    list_sum = 0
    while list_num:
        if len(list_num) == 1:
            # 개수가 하나 남을 경우
            list_sum += list_num.pop()
        else:
            list_sum += list_num.pop() * list_num.pop()
    return list_sum


num = []
minus = []
one = []

for _ in range(int(input())):
    a = int(input())
    if a == 1:
        one.append(a)
    elif a > 0:
        num.append(a)
    else:
        minus.append(a)

num.sort()
minus.sort(reverse=True)

answer = 0
answer += check(num)
answer += check(minus)
answer += sum(one)
print(answer)
