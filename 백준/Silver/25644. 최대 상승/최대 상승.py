n = int(input())
stocks = list(map(int, input().split()))

min_price = stocks[0]
max_profit = 0

for price in stocks[1:]:
    profit = price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price)

print(max_profit)