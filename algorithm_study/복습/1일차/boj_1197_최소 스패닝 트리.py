import sys
sys.setrecursionlimit(10**6)  # 재귀 호출 한도를 늘림

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    pX, pY = find(x), find(y)
    if pX > pY:
        parent[pX] = pY
    else:
        parent[pY] = pX

V, E = map(int, sys.stdin.readline().split())
arr, parent = [], [i for i in range(V)]  # 초기에는 자기 자신을 부모로 설정

for _ in range(E):
    v1, v2, dist = map(int, sys.stdin.readline().split())
    arr.append((dist, v1-1, v2-1))
arr.sort()

mst = 0
for a in arr:
    if find(a[1]) == find(a[2]):
        continue
    union(a[1], a[2])
    mst += a[0]

print(mst)