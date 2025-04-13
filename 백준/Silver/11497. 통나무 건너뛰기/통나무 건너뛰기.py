from collections import deque
t = int(input())

def make(list, start):
    is_left = start
    result = deque()
    for i in list:
        if is_left:
            result.append(i)
            is_left = False
        else:
            result.appendleft(i)
            is_left = True
    max_data = 0
    for i in range(1, len(list)):
        max_data = max(max_data, abs(result[i-1] - result[i]))
    max_data = max(max_data, abs(result[0] - result[-1]))
    return max_data


for _ in range(t):
    n = int(input())
    logs = list(map(int, input().split()))
    logs.sort(reverse=True)

    start_left = make(logs, True)
    start_right = make(logs, False)

    print(min(start_left, start_right))