from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2
    if total % 2:  # 전체 합이 홀수면 불가능
        return -1
    target = total // 2

    ops = 0
    limit = 3 * len(q1)  # 안전한 상한 (경험적으로 충분)

    while s1 != target and ops <= limit:
        if s1 > target:
            x = q1.popleft()
            s1 -= x
            q2.append(x)
            s2 += x
        else:
            x = q2.popleft()
            s2 -= x
            q1.append(x)
            s1 += x
        ops += 1

    return ops if s1 == target else -1
