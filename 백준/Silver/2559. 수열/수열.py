import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

prefix_sum = sum(temps[:k])
max_sum = prefix_sum

for i in range(k, n):
    prefix_sum += temps[i] - temps[i - k]
    if prefix_sum > max_sum:
        max_sum = prefix_sum

print(max_sum)