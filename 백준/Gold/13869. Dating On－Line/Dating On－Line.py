from collections import deque
import math
n = int(input())
status_list = sorted(list(map(int, input().split())), reverse=True)

result = []

for i in range(2):
    left = i
    q = deque()
    for status in status_list:
        if left == 0:
            q.append(status)
            left = 1
        else:
            q.appendleft(status)
            left = 0
    result.append(q)

max_result = 0
theta = 2 * math.pi / n
for lines in result:
    cal_status = 0
    for i in range(1, len(lines)):
        cal_status += 0.5 * lines[i-1] * lines[i] * math.sin(theta)
    cal_status += 0.5 * lines[0] * lines[-1] * math.sin(theta)
    max_result = max(max_result, cal_status)

print(f"{max_result:.3f}")