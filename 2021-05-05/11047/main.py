count, amount = map(int, input().split())  # 동전 종류, 원하는 액수 입력
kind = []  # 동전 종류 입력 배열 변수
for i in range(count):
    kind.append(int(input()))

kind.sort()  # 배열 정렬
answer = 0
for i in range(len(kind)-1, -1, -1):  # 동전 종류의 역순으로 반복
    c = amount // kind[i]  # 총액을 해당 동전으로 나눈 몫
    answer += c
    amount -= (kind[i]*c)
print(answer)
