from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(input()[:-1]) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs():
    global meet_person
    while q:
        x, y = q.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and campus[nx][ny] != "X":
                    if campus[nx][ny] == "P":
                        meet_person += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return meet_person
q = deque()
meet_person = 0


for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            q.append((i,j))
            visited[i][j] = True
            meet_person = bfs()

if meet_person == 0:
    print("TT")
else:
    print(meet_person)