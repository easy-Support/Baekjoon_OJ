k = [int(input()) for _ in range(int(input()))]
k.sort(reverse=True)

max = 0
for i in range(len(k)):
    if k[i] * (i + 1) > max:
        max = k[i] * (i + 1)
print(max)
