from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
cost = [0] * (n+1)
result = [0] * (n+1)
q = deque()


for i in range(1, n+1):
    input_data = list(map(int, input().split()))
    data = input_data[1:]
    cost[i] = input_data[0]
    for j in data:
        if j != -1:
            graph[j].append(i)
            in_degree[i] += 1


for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)


while q:
    current = q.popleft()
    result[current] += cost[current]
    for i in graph[current]:
        in_degree[i] -= 1
        result[i] = max(result[i], result[current])
        if in_degree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])