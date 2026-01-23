import sys
input = sys.stdin.readline

n = int(input().strip())
best_i, best_L = 1, None

for i in range(1, n+1):
    j, m = map(int, input().split())
    L = 2 * ((j - 1) // (m + 1) + 1)
    if best_L is None or L < best_L:
        best_L = L
        best_i = i

print(best_i, best_L)
