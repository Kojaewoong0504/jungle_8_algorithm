import sys
sys.setrecursionlimit(10**5*6) # 정점이 50만까지 들어가기에, 호출 깊이가 50만까지 가능해야함.
input=sys.stdin.readline
 
def dfs(root):
    visited[root]=1
    for next_node in graph[root]:
        if not visited[next_node]:
            paths[next_node]=paths[root]+1 # 루트로부터 해당노드까지의 거리 갱신
            dfs(next_node)
 
 
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
 
for _ in range(n-1):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
 
paths=[0]*(n+1) # 루트~각노드까지의 거리 저장
dfs(1)
print('YNeos'[sum(paths[i] for i in range(2,n+1) if len(graph[i])==1)%2==0::2])
