import sys

a_1, b_1 = map(int, sys.stdin.readline().split())
a_2, b_2 = map(int, sys.stdin.readline().split())

print(min(a_1 + b_2, a_2 + b_1))
