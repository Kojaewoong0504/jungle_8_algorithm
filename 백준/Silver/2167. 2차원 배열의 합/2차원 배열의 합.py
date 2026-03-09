n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = (
            prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
            + nums[i-1][j-1]
        )

k = int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    result = (
        prefix[x][y]
        - prefix[i-1][y]
        - prefix[x][j-1]
        + prefix[i-1][j-1]
    )
    print(result)