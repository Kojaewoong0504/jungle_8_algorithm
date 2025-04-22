from collections import deque

n, k = map(int, input().split())

p_list = deque([i for i in range(1, n+1)])
result = []

while p_list:
    p_list.rotate(-(k-1))
    result.append(p_list.popleft())

print(f"<{', '.join(map(str, result))}>")