from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 0: 미감염, 1~3: 바이러스, -1: 치료제
result = [row[:] for row in maps]
arrival_time = [[-1] * m for _ in range(n)]
virus_map = [[0] * m for _ in range(n)]

q = deque()

# 초기 바이러스 큐 삽입
for i in range(n):
    for j in range(m):
        if maps[i][j] in [1, 2]:
            q.append((i, j, 0, maps[i][j]))
            arrival_time[i][j] = 0
            virus_map[i][j] = maps[i][j]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x, t, v = q.popleft()

    if result[y][x] == 3:  # 3번 바이러스는 전염 불가
        continue

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] == -1 or result[ny][nx] == 3:
                continue

            if arrival_time[ny][nx] == -1:
                # 처음 도달
                arrival_time[ny][nx] = t + 1
                virus_map[ny][nx] = v
                result[ny][nx] = v
                q.append((ny, nx, t + 1, v))
            elif arrival_time[ny][nx] == t + 1:
                # 동시 도달
                if virus_map[ny][nx] != v and virus_map[ny][nx] in [1, 2]:
                    result[ny][nx] = 3  # 3번 바이러스로 전환
                    virus_map[ny][nx] = 3  # 이후 더 이상 퍼지지 않음

# 결과 세기
count = [0, 0, 0, 0]
for i in range(n):
    for j in range(m):
        if result[i][j] in [1, 2, 3]:
            count[result[i][j]] += 1

print(count[1], count[2], count[3])
