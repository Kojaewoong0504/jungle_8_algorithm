import sys
input = sys.stdin.readline


R, C, k = map(int, input().split())

maps = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

count = 0


def dfs(r, c, depth):
    global count
    if depth == k:
        if r == 0 and c == C - 1:
            count += 1
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if maps[nr][nc] != "T" and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, depth + 1)
                visited[nr][nc] = False


visited[R - 1][0] = True
dfs(R - 1, 0, 1)
print(count)
