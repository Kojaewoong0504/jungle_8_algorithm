import sys
from collections import deque, defaultdict
input = sys.stdin.readline

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs():
    result = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    lights = [[0 for _ in range(n)] for _ in range(n)]
    lights[0][0] = 1

    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for tr, tc in turn_light[(r, c)]:
            if not lights[tr][tc]:
                lights[tr][tc] = 1
                result += 1
                for d in direction:
                    nr = tr + d[0]
                    nc = tc + d[1]
                    if 0 <= nr < n and 0 <= nc < n:
                        if visited[nr][nc]:
                            lights[nr][nc] = 1
                            q.append((nr, nc))
        for d in direction:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and lights[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    return result


n, m = map(int, input().split())
turn_light = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    turn_light[(x - 1, y - 1)].append((a - 1, b - 1))

print(bfs())