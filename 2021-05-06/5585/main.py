amount = 1000 - int(input())
kind = [500, 100, 50, 10, 5, 1]

answer = 0
for i in kind:
    answer += amount // i
    amount %= i
print(answer)
