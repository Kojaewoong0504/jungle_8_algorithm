from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

buffer = deque()

while True:
    input_data = int(input())
    if input_data < 0:
        break
    if input_data > 0:
        if len(buffer) < n:
            buffer.append(input_data)
    else:
        buffer.popleft()

if buffer:
    print(' '.join(map(str, buffer)))
else:
    print("empty")