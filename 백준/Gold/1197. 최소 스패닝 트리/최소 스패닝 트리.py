import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)] 
in_graph = [False]*(V+1)

for _ in range(E) :
    v1, v2, weight = map(int, input().split())
    graph[v1].append((weight, v2))
    graph[v2].append((weight, v1))

node_cnt = 0 #그래프에 포함된 노드 개수
weight_sum = 0

#그래프에 포함된 노드들에 인접한 간선 모음
edge_heap = [(0,1)] #가중치, 새로 추가될 노드번호
while node_cnt < V :
    w, node = heapq.heappop(edge_heap)

    #이미 그래프에 포함된 노드면 패스
    if in_graph[node] :
        continue

    #새로운 노드 추가
    in_graph[node] = True
    node_cnt += 1
    weight_sum += w

    #새로 추가된 노드의 간선들을 힙에 추가
    for edge in graph[node] :
        heapq.heappush(edge_heap, edge)

print(weight_sum)