from collections import deque
n = int(input())

people = [i for i in range(1, n+1)]
q = deque(people)

result = []
result.append(q.popleft())
t = 2
while q:
    rotate = (t**3)-1
    q.rotate(-rotate)
    result.append(q.popleft())
    t += 1


print(result[-1])