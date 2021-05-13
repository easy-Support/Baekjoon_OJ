count = int(input())
answer = 0

while count > 0:
    if count % 5 == 0:
        count -= 5
        answer += 1
    elif count % 3 == 0:
        count -= 3
        answer += 1
    elif count > 5:
        count -= 5
        answer += 1
    else:
        answer = -1
        break
print(answer)