import sys

input = sys.stdin.readline
R, C = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 1


def dfs(r, c, visited, count):
    global result
    result = max(result, count)

    # 이미 26개의 알파벳을 모두 방문했거나, 가능한 모든 칸을 방문했다면 종료
    if result == 26 or result == R * C:
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            alpha_idx = ord(board[nr][nc]) - ord('A')
            if not (visited & (1 << alpha_idx)):
                dfs(nr, nc, visited | (1 << alpha_idx), count + 1)


board = [list(input().strip()) for _ in range(R)]
start_alpha_idx = ord(board[0][0]) - ord('A')
dfs(0, 0, 1 << start_alpha_idx, 1)
print(result)
