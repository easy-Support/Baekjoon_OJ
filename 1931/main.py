count = int(input())  # 회의실 개수 입력

kind = []
for _ in range(count):
    kind.append(list(map(int, input().split())))

kind.sort(key=lambda x: x[0])  # 2차원 배열 첫번째 수로 오름차순 정렬
kind.sort(key=lambda x: x[1])  # 2차원 배열 두번째 수로 오름차순 정렬

last, answer = 0, 0

for start, end in kind:
    if last <= start:  # 마지막 시간이 첫번째 시간보다 작거나 같을 경우
        last = end
        answer += 1
print(answer)
