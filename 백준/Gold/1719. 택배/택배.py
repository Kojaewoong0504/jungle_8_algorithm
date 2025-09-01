import sys
input = sys.stdin.readline

INF = 10**9

n, m = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
nxt = [[-1] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c
        nxt[a][b] = b
        nxt[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        if i == j:
            row.append('-')
        else:
            row.append(str(nxt[i][j]))
    print(' '.join(row))
