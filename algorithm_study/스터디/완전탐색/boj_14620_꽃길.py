from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

can_list = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        can_list.append((i, j, board[i][j]))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

min_cost = float('inf')
for comb in combinations(can_list, 3):
    is_can = True
    visited = [[False for _ in range(n)] for _ in range(n)]
    total_cost = 0
    for y, x, cost in comb:
        total_cost += cost
        if visited[y][x]:
            is_can = False
            break
        visited[y][x] = True
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]
            if visited[ny][nx]:
                is_can = False
                break
            total_cost += board[ny][nx]
            visited[ny][nx] = True
    if is_can:
        min_cost = min(min_cost, total_cost)

print(min_cost)
