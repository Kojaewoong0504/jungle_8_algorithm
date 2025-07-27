from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    h, w, o, force, xs, ys, xe, ye = map(int, input().split())

    field = [[0 for _ in range(w)] for _ in range(h)]
    xs, ys, xe, ye = xs - 1, ys - 1, xe - 1, ye - 1
    for _ in range(o):
        x, y, l = map(int, input().split())
        field[x - 1][y - 1] = l

    q = deque()
    q.append((xs, ys, force))
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    visited[xs][ys] = force

    is_success = False
    while q:
        x, y, f = q.popleft()
        if x == xe and y == ye:
            is_success = True
            break
        if f <= 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                height_diff = field[nx][ny] - field[x][y]
                if height_diff <= f:
                    nf = f - 1
                    if visited[nx][ny] < nf:
                        visited[nx][ny] = nf
                        q.append((nx, ny, nf))
    if is_success:
        print("잘했어!!")
    else:
        print("인성 문제있어??")
