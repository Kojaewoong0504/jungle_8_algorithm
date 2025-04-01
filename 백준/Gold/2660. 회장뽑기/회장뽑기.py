import math
import sys

input = sys.stdin.readline

n = int(input())
board = [[math.inf if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]
a, b = map(int, input().split())
while a != -1:
    board[a][b] = 1
    board[b][a] = 1
    a, b = map(int, input().split())


def floyd_warchall(graph):
    # 플루이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


result = floyd_warchall(board)
ans = {}
for i in range(1, n + 1):
    ans[i] = max(result[i][1:])

min_score = min(ans.values())
print(min_score, list(ans.values()).count(min_score))
for key, value in ans.items():
    if value == min_score:
        print(key, end=' ')