import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def scc(G, V):
    finished = [False] * (V + 1)
    label = [0]  # 누적 라벨: 노드를 한번 방문할 때마다 1씩 증가
    labels = [0] * (V + 1)  # 고유 라벨 번호 저장
    ans, stack = [], []

    def _scc(u):
        label[0] += 1
        parent = labels[u] = label[0]  # 자기 자신이 부모노드로 가정
        stack.append(u)

        for v in G[u]:
            if not labels[v]:  # 아직 방문 X
                parent = min(parent, _scc(v))
            elif not finished[v]:  # 방문은 했지만 SCC 처리가 아직 안된 노드
                parent = min(parent, labels[v])

        # 부모 노드가 자기 자신이라면 => 루트 노드
        if parent == labels[u]:
            scc_set = []
            while True:
                p = stack.pop()
                scc_set.append(p)
                finished[p] = True
                if p == u:
                    break
            ans.append(scc_set)

        return parent

    # 모든 노드에 대해 방문되지 않았다면 SCC 구하기
    for node in range(1, V + 1):
        if not labels[node]:
            _scc(node)

    return ans

# 입력 받기
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)

# SCC 구하기
ans = scc(graph, v)

# 각 SCC 내부 정렬
for component in ans:
    component.sort()
# 첫 원소 기준으로 전체 정렬
ans.sort(key=lambda x: x[0])

# 결과 출력
print(len(ans))
for component in ans:
    print(*component, -1)
