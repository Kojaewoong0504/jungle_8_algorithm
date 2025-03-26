from collections import deque


def solve(N, M, K):
    # 상태: (창의인재관 학생 수, 창의인재관 우산 수, 융합인재관 학생 수, 융합인재관 우산 수, 시행 횟수)
    queue = deque([(N, M, 0, 0, 0)])
    visited = set([(N, M, 0, 0)])  # 방문한 상태 기록 (시행 횟수 제외)

    while queue:
        a, b, c, d, steps = queue.popleft()

        # 목표 상태 도달: 모든 학생이 융합인재관에 있음
        if c == N:
            return steps

        # 1. 창의인재관에서 융합인재관으로 이동
        for x in range(1, a + 1):  # 이동할 학생 수
            for y in range(1, b + 1):  # 사용할 우산 수
                if x <= K * y:  # 우산 용량 조건
                    new_state = (a - x, b - y, c + x, d + y)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((*new_state, steps + 1))

        # 2. 융합인재관에서 창의인재관으로 이동
        for z in range(1, c + 1):  # 이동할 학생 수
            for w in range(1, d + 1):  # 사용할 우산 수
                if z <= K * w:  # 우산 용량 조건
                    new_state = (a + z, b + w, c - z, d - w)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((*new_state, steps + 1))

    # 목표 상태에 도달할 수 없음
    return -1


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    print(solve(N, M, K))
