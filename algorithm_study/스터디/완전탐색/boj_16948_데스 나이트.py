from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1
    while q:
        r, c = q.popleft()
        if r == r2 and c == c2:
            return visited[r][c] - 1

        for dr, dc in direction:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return -1


print(bfs(r1,c1))
