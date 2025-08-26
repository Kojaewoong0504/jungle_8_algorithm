import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n, m = map(int, input().split())

lists = []
question = []

for _ in range(n):
    lists.append(int(input()))

for _ in range(m):
    question.append(int(input()))

lists.sort()

for i in range(m):
    left = bisect_left(lists, question[i])
    right = bisect_right(lists, question[i])
    if left == right:
        print(-1)
    else:
        print(left)