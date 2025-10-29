from collections import defaultdict

N, M = map(int, input().split())
rank = [0] + list(map(int, input().split()))

board = defaultdict(list)
for n in range(1, N+1):
    lst = list(map(int, input().split()))[1:]
    for k in lst:
        board[k].append(n)

for k in board:
    board[k].sort(key=lambda x: rank[x])

Q = int(input())
for _ in range(Q):
    k = int(input())
    if board[k]:
        print(*board[k])
    else:
        print(-1)