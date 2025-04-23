import sys

input = sys.stdin.readline
from collections import Counter


def check(string):
    for t in target:
        if t in string and string[t] != 0:
            string[t] -= 1
        else:
            return False
    return True


target = input().strip()
N = int(input())
prices = []
for n in range(N):
    price, title = map(str, input().strip().split())
    prices.append([int(price), Counter(title)])
result = float('inf')

for i in range(1 << N):
    price = 0
    alpha = Counter()
    for j in range(N):
        if (i & 1 << j):
            price += prices[j][0]
            alpha += prices[j][1]

    if check(alpha):
        result = min(result, price)

print(result if not result == float('inf') else -1)
