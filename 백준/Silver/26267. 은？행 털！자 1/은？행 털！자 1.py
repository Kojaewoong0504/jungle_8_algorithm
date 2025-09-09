import sys
input = sys.stdin.readline

n = int(input())
datas = {}

for _ in range(n):
    x, t, c = map(int, input().split())
    d = x - t
    datas[d] = datas.get(d, 0) + c

print(max(datas.values()))