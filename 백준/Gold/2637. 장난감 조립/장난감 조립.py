from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

in_degree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
parts_info = [[] for _ in range(n+1)]


for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append(x)
    in_degree[x] += 1
    parts_info[x].append((y, k))


result = []
q = deque()


for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)

# 각 부품별 필요한 기본 부품 개수 계산
# dp[i][j]: i번 부품을 만드는데 필요한 j번 기본 부품의 개수
dp = [[0] * (n+1) for _ in range(n+1)]

# 기본 부품 초기화 (자기 자신은 1개)
for i in range(1, n+1):
    if not parts_info[i]:  # 기본 부품인 경우
        dp[i][i] = 1

# 위상 정렬 결과를 이용해 부품별 필요 개수 계산
for part in result:
    # 현재 부품이 중간 부품이나 완제품인 경우
    for needed_part, count in parts_info[part]:
        # 필요한 부품이 기본 부품인 경우
        if not parts_info[needed_part]:
            dp[part][needed_part] += count
        # 필요한 부품이 중간 부품인 경우
        else:
            for i in range(1, n+1):
                dp[part][i] += dp[needed_part][i] * count

# 결과 출력 (기본 부품만)
for i in range(1, n):
    if not parts_info[i] and dp[n][i] > 0:  # i가 기본 부품이고, 완제품에 필요한 경우
        print(i, dp[n][i])