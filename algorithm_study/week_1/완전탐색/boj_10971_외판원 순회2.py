import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_result = float('INF')

def dfs(current, count, cost):
    global min_result

    if count == n:
        # 추가적으로 해당 도시에서 첫 도시로 이동할 수 있는지 확인하고 이동 비용을 계산해야 한다.
        if city[current][0] != 0:
            min_result = min(min_result, cost + city[current][0])
        return

    for next_city in range(n):
        # 조건 - 이동하려는 도시가 현재 도시에서 연결되었는지 확인한다.
        if not visited[next_city] and city[current][next_city] != 0:
            visited[next_city] = True
            dfs(next_city, count + 1, cost + city[current][next_city])
            visited[next_city] = False
    return min_result


visited[0] = True
print(dfs(0, 1, 0))