from collections import deque
import math, sys

input = sys.stdin.readline
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

# import math
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def make_zigzag(arr, start_left: bool):
#     dq = deque()
#     left = start_left
#     for val in arr:
#         if left:
#             dq.appendleft(val)
#         else:
#             dq.append(val)
#         left = not left
#     return list(dq)
#
# def calculate_area(points, theta):
#     area = 0
#     for i in range(len(points)):
#         a = points[i]
#         b = points[(i + 1) % len(points)]
#         area += 0.5 * a * b * math.sin(theta)
#     return area
#
# n = int(input())
# scores = list(map(int, input().split()))
# scores.sort(reverse=True)
#
# theta = 2 * math.pi / n
# max_area = 0
#
# # 두 가지 지그재그 배치 모두 시도
# for start_left in (False, True):
#     zigzag = make_zigzag(scores, start_left)
#     area = calculate_area(zigzag, theta)
#     max_area = max(max_area, area)
#
# print(f"{max_area:.3f}")
