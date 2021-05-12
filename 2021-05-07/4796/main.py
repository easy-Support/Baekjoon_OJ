import sys

index = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())

    if L + P + V == 0:
        break

    print("Case %d: %d" % (index, ((V//P) * L) + min((V%P), L)))
    index += 1
