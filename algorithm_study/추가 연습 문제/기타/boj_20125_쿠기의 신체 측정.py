from collections import deque

n = int(input())

cookies = [list(input()) for i in range(n)]

q = deque()

bodies = [0] * 5
heart = []

for i in range(n):
    for j in range(n):
        if cookies[i][j] == "*":
            q.append((i+1,j+1))

head = q.popleft()
heart = (head[0]+1,head[1])
while q:
    x,y = q.popleft()
    if x == heart[0] and y == heart[1]:
        continue
    if y < heart[1] and x == heart[0]:
        bodies[0] += 1
    elif y > heart[1] and x == heart[0]:
        bodies[1] += 1
    elif y == heart[1] and x > heart[0]:
        bodies[2] += 1
    elif y == (heart[1]-1) and x > heart[0]:
        bodies[3] += 1
    elif y == (heart[1]+1) and x > heart[0]:
        bodies[4] += 1

print(" ".join(map(str, heart)))
print(" ".join(map(str, bodies)))
