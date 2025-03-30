import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(start_x, start_y, h, w, grid):
    dist = [[INF] * (w + 2) for _ in range(h + 2)]
    heap = []
    dist[start_x][start_y] = 0
    heappush(heap, (0, start_x, start_y))

    while heap:
        cost, x, y = heappop(heap)
        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if grid[nx][ny] == '*':
                    continue
                new_cost = cost + (1 if grid[nx][ny] == '#' else 0)
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heappush(heap, (new_cost, nx, ny))
    return dist


def solve():
    h, w = map(int, input().split())
    grid = [['.'] * (w + 2)]
    prisoners = []

    # 외곽 확장 및 입력 처리
    for i in range(1, h + 1):
        line = ['.'] + list(input().strip()) + ['.']
        grid.append(line)
        for j in range(w + 2):
            if line[j] == '$':
                prisoners.append((i, j))
    grid.append(['.'] * (w + 2))

    # 3개의 시작점에서 최단거리 계산
    dist0 = dijkstra(0, 0, h, w, grid)  # 상근이
    dist1 = dijkstra(*prisoners[0], h, w, grid)
    dist2 = dijkstra(*prisoners[1], h, w, grid)

    # 모든 좌표에서 합산 최소값 찾기
    min_doors = INF
    for i in range(h + 2):
        for j in range(w + 2):
            total = dist0[i][j] + dist1[i][j] + dist2[i][j]
            if grid[i][j] == '#':  # 중복 카운트 보정
                total -= 2
            min_doors = min(min_doors, total)

    print(min_doors)


t = int(input())
for _ in range(t):
    solve()
