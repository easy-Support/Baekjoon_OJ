import sys

int(input())
city_length = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))

min_price = oil_price[0]  # 최저가
price = 0
for i in range(len(city_length)):
    if oil_price[i] <= min_price:  # 최저가
        min_price = oil_price[i]
    price += min_price * city_length[i]

print(price)
