import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

result = [row[:] for row in maps]
arrival = [[-1] * m for _ in range(n)]
hq = []

# 초기 감염 상태 저장
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 or maps[i][j] == 2:
            heapq.heappush(hq, (0, maps[i][j], i, j))
            arrival[i][j] = 0  # 감염 시작점은 시간 0에 도착한 걸로

dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while hq:
    time, virus, y, x = heapq.heappop(hq)

    # 이미 3번 바이러스로 바뀐 경우는 전염 못함
    if result[y][x] == 3 or maps[y][x] == -1:
        continue

    for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] == -1 or result[ny][nx] == 3:
                continue

            if arrival[ny][nx] == -1:
                # 처음 도달한 경우
                arrival[ny][nx] = time + 1
                result[ny][nx] = virus
                heapq.heappush(hq, (time + 1, virus, ny, nx))
            elif arrival[ny][nx] == time + 1:
                # 다른 바이러스가 동시에 도달해 있다면 → 3번 바이러스
                if result[ny][nx] != virus and result[ny][nx] in [1, 2]:
                    result[ny][nx] = 3

# 결과 세기
count = [0, 0, 0, 0]
for i in range(n):
    for j in range(m):
        if result[i][j] in [1, 2, 3]:
            count[result[i][j]] += 1

print(count[1], count[2], count[3])