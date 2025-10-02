import sys
input = sys.stdin.readline

K = int(input().strip())
arr = list(map(int, input().split()))
levels = [[] for _ in range(K)]

def build(l, r, depth):
    if l > r:
        return
    mid = (l + r) // 2
    levels[depth].append(arr[mid])
    build(l, mid - 1, depth + 1)
    build(mid + 1, r, depth + 1)

build(0, len(arr) - 1, 0)

for d in range(K):
    print(*levels[d])
