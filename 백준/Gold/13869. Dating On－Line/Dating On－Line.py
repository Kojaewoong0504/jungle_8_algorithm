import math
import sys
from collections import deque

input = sys.stdin.readline

def make_zigzag(arr, start_left: bool):
    dq = deque()
    left = start_left
    for val in arr:
        if left:
            dq.appendleft(val)
        else:
            dq.append(val)
        left = not left
    return list(dq)

def calculate_area(points, theta):
    area = 0
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        area += 0.5 * a * b * math.sin(theta)
    return area

n = int(input())
scores = list(map(int, input().split()))
scores.sort(reverse=True)

theta = 2 * math.pi / n
max_area = 0

# 두 가지 지그재그 배치 모두 시도
for start_left in (False, True):
    zigzag = make_zigzag(scores, start_left)
    area = calculate_area(zigzag, theta)
    max_area = max(max_area, area)

print(f"{max_area:.3f}")