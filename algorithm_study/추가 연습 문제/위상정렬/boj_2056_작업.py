from collections import deque

n = int(input())

time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 입력 처리
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 작업 시간

    # 선행 작업이 있는 경우
    if len(data) > 1:
        prereq_count = data[1]  # 선행 작업 개수

        if prereq_count > 0:
            for j in range(2, 2 + prereq_count):
                prev_task = data[j]
                graph[prev_task].append(i)  # prev_task -> i 방향으로 간선 추가
                indegree[i] += 1  # i의 진입차수 증가


# 위상 정렬 함수
def topology_sort():
    result = time.copy()  # 각 작업의 최소 완료 시간 (기본값은 자신의 작업 시간)
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 위상 정렬 수행
    while q:
        now = q.popleft()

        # 해당 노드와 연결된 노드들의 진입차수 감소
        for next_node in graph[now]:
            indegree[next_node] -= 1
            # 선행 작업 완료 시간 + 현재 작업 시간과 기존 값 비교하여 최대값 선택
            result[next_node] = max(result[next_node], result[now] + time[next_node])

            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[next_node] == 0:
                q.append(next_node)

    # 모든 노드 중 최대 완료 시간 반환
    return max(result[1:])


print(topology_sort())
