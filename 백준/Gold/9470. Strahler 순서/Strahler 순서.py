from collections import deque, defaultdict

t = int(input())


def topology_sort():
    q = deque()
    order = [0] * (m+1)
    count = [defaultdict(int) for _ in range(m+1)]
    for i in range(1, m+1):
        if in_degree[i] == 0:
            q.append(i)
            order[i] = 1

    while q:
        cur = q.popleft()

        for next_node in graph[cur]:
            count[next_node][order[cur]] += 1

            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                max_order = max(count[next_node].keys())
                if count [next_node][max_order] >= 2:
                    order[next_node] = max_order + 1
                else:
                    order[next_node] = max_order
                q.append(next_node)
    return  order[m]




for _ in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m+1)]
    in_degree = [0] * (m+1)

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    result = topology_sort()
    print(k, result)

