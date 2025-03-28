import sys

sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())  # 정점수
A = [0] + list(map(int, sys.stdin.readline().strip()))  # 실외 실내 정보를 노드 인덱스 1과 맞추기 위해 [0] 추가
tree = [[] for _ in range(N + 1)]  # 빈공간 생성
visit = [0] * (N + 1)  # 방문 체크
ans = 0
res = 0
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    if A[a] == 1 and A[b] == 1:  # 둘다 실내일때 경우
        ans += 2  # 서로 방문하는 케이스가 2개


def dfs(v, cnt):  # cnt 실외와 연결된 실내 노드 개수
    visit[v] = 1
    for i in tree[v]:
        if A[i] == 0 and visit[i] == 0:  # 내 외 내 내 외 일경우 마지막 외가 카운팅 안되는 반례
            cnt = dfs(i, cnt)  # 해당 실외 기점으로 재귀
        elif A[i] == 1 and visit[i] == 0:  # 실내면서 방문하지않았다면
            cnt += 1
    return cnt


for i in range(1, N + 1):
    if visit[i] == 0 and A[i] == 0:  # 방문안한 실외를 기준으로
        x = dfs(i, 0)  # dfs시작 cnt는 시작이 0
        res += x * (x - 1)  # 실외를 기준으로 인접한 실내 점 n개가 있을때 경로는 n(n-1)개이다

print(res + ans)