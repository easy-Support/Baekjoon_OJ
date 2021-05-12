count = int(input())
time = list(map(int, input().split()))
time.sort()

account = 0
for i in range(count):
    for j in range(i+1):
        account += time[j]
print(account)
