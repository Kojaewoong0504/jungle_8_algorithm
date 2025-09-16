from collections import deque

def solution(priorities, location):
    count = 0
    q = deque()
    for priority in range(len(priorities)):
        q.append((priorities[priority], priority))

    while q:
        _priority, idx = q.popleft()
        if q and max(p for p, _ in q) > _priority:
            q.append((_priority, idx))
        else:
            count += 1
            if idx == location:
                return count
