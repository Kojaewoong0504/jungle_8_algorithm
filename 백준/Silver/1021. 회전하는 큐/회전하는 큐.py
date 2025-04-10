from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

count = 0
for i in position:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2:
                while q[0] != i:
                    q.append(q.popleft())
                    count += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    count += 1
print(count)