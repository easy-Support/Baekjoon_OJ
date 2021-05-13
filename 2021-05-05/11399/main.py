count = int(input())  # 사람의 수 입력
time = list(map(int, input().split()))  # 사람 당 인출하는데 걸리는 시간 입력
time.sort()  # 오름차순으로 정렬

account = 0
for i in range(count):
    for j in range(i+1):
        account += time[j]
print(account)
