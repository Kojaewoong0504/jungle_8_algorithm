import sys

input = sys.stdin.readline
n = int(input())

stick = [int(input()) for _ in range(n)]

right = stick[-1]

cnt = 1
for i in range(len(stick)-2, -1,-1):
    if stick[i] > right:
        right = stick[i]
        cnt +=1

print(cnt)