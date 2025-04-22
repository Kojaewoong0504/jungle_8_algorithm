from collections import deque

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]

def bfs(start, shark_size, graph, N):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((start[0], start[1], 0))  # (x, y, distance)
    visited[start[0]][start[1]] = True
    fishes = []

    directions = [(-1,0), (0,-1), (0,1), (1,0)]  # 위, 왼, 오, 아래 우선순위

    while q:
        x, y, dist = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                cell = graph[nx][ny]
                if cell <= shark_size:  # 지나갈 수 있는 칸
                    visited[nx][ny] = True
                    if 0 < cell < shark_size:
                        fishes.append((dist + 1, nx, ny))
                    q.append((nx, ny, dist + 1))

    return sorted(fishes)  # 거리 → 위 → 왼 순 정렬


def solve(graph, N):
    # 상어 위치 및 초기 설정
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                shark_pos = (i, j)
                graph[i][j] = 0

    time = 0
    size = 2
    eaten = 0

    while True:
        candidates = bfs(shark_pos, size, graph, N)
        if not candidates:
            break

        dist, x, y = candidates[0]
        time += dist
        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0

        graph[x][y] = 0
        shark_pos = (x, y)

    return time


print(solve(sea, n))