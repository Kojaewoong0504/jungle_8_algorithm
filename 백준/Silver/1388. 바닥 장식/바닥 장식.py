n, m = map(int, input().split())
room = [input().rstrip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            visited[i][j] = True

            if room[i][j] == '-':
                nj = j + 1
                while nj < m and room[i][nj] == '-':
                    visited[i][nj] = True
                    nj += 1

            else:
                ni = i + 1
                while ni < n and room[ni][j] == '|':
                    visited[ni][j] = True
                    ni += 1

print(count)
