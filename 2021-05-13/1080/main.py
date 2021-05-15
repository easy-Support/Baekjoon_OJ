import sys


def turn(c_list, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            c_list[i][j] = 1 - c_list[i][j]
    return c_list


n, m = map(int, sys.stdin.readline().split())
a_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

answer = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a_list[i][j] != b_list[i][j]:
            a_list = turn(a_list, i, j)
            answer += 1

if a_list == b_list:
    print(answer)
else:
    print(-1)
