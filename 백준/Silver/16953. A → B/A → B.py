from collections import deque


def min_operations(A, B):
    if A > B:
        return -1

    visited = set()
    q = deque([(B, 0)])  # (숫자, 연산 횟수)

    while q:
        num, ops = q.popleft()

        if num == A:
            return ops + 1  # 문제 요구사항: 최소 연산 횟수 + 1

        # B가 짝수인 경우: 2로 나누기 (역연산)
        if num % 2 == 0:
            next_num = num // 2
            if next_num >= A and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, ops + 1))

        # B가 1로 끝나는 경우: 마지막 1 제거하고 10으로 나누기 (역연산)
        if num % 10 == 1:
            next_num = (num - 1) // 10
            if next_num >= A and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, ops + 1))

    return -1  # 변환 불가능


A, B = map(int, input().split())
print(min_operations(A, B))
