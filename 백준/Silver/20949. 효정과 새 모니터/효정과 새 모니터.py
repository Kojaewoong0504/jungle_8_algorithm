import sys
input = sys.stdin.readline

N = int(input())
items = []
for i in range(1, N+1):
    W, H = map(int, input().split())
    s = W*W + H*H
    items.append((-s, i))

items.sort()
for _, idx in items:
    print(idx)
