import sys
sys.setrecursionlimit(10000)

dw = [-1,1,0,0,1,1,-1,-1]
dh = [0,0,-1,1,1,-1,1,-1]


def dfs(high, weight):
    for i in range(8):
        nh = high + dh[i]
        nw = weight + dw[i]
        if 0 <= nw < w and 0 <= nh < h:
            if not visited[nh][nw] and maps[nh][nw] == 1:
                visited[nh][nw] = True
                dfs(nh, nw)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
            else:
                continue
    print(cnt)