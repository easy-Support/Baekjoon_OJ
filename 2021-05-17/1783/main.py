# N : 세로 / M : 가로
N, M = map(int, input().split())

if N == 1:
    # 세로가 1일 경우
    answer = 1
elif N == 2:
    # 세로가 2일 경우
    answer = min(4, (M + 1) // 2)
else:
    # 세로가 1, 2이 아닌 경우
    if M >= 7:
        # 가로가 7 이상일 경우
        answer = M - 2
    else:
        # 가로가 7 미만일 경우
        answer = min(4, M)
print(answer)
