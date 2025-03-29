n, m = map(int, input().split())

edges = []
INF = int(1e18)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))


def bellman_ford(start):

    distance[start] = 0

    # n-1번 라운드 반복
    for i in range(n - 1):
        updated = False
        for edge in edges:
            cur, next_node, cost = edge
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                updated = True
        if not updated:  # 더 이상 갱신되지 않으면 조기 종료
            break

    # 음수 사이클 확인 (n번째 라운드)
    has_negative_cycle = False
    for edge in edges:
        cur, next_node, cost = edge
        if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
            has_negative_cycle = True
            break
    return has_negative_cycle


negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(-1 if distance[i] == INF else distance[i])