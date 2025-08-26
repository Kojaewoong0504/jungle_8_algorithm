import sys
input = sys.stdin.readline

n = int(input())
big = list(input().strip() for _ in range(n)) #대근
zero = list(input().strip() for _ in range(n)) #영식

visited = set()
i = 0
ans = 0

for car in zero:
    while i < n and big[i] in visited:
        i += 1
    if i < n and big[i] == car:
        visited.add(car)
        i += 1
    else:
        visited.add(car)
        ans += 1

print(ans)

