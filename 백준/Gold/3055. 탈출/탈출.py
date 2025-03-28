import sys
from collections import deque
R, C = map(int, input().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

for y in range(R):
    for x in range(C):
        if map[y][x] == '*':
            q.appendleft((y, x))
        elif map[y][x] == 'S':
            q.append((y, x))
            visited[y][x] = 0

while q:
    y, x = q.popleft()
    cur = map[y][x]  # 현재 위치
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]  # 다음에 갈 좌표

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 범위 밖이면 무시
            continue
        if visited[ny][nx] != -1:  # 이미 방문한 곳 무시
            continue
        if map[ny][nx] == "*":  # 물 무시
            continue
        if map[ny][nx] == "X":  # 돌 무시
            continue
        if cur == "*" and map[ny][nx] == "D":
            continue

        if cur == "S":
            if map[ny][nx] == "D":
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1

        map[ny][nx] = cur
        q.append((ny, nx))
    else:
        continue
    break
else:
    print("KAKTUS")