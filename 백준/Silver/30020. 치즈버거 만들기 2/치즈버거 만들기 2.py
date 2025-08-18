import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a <= b or a > 2 * b:
    print("NO")
    exit(0)

k = a-b
print("YES")
print(k)

cheese_counts = [1] * k
remaining = b - k

for i in range(remaining):
    cheese_counts[i % k] += 1

for c in cheese_counts:
    burger = "a" + "ba" * c
    print(burger)