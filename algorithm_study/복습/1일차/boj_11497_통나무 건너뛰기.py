from collections import deque


t = int(input())

for _ in range(t):
    n = int(input())

    log_list = sorted(list(map(int, input().split())), reverse=True)

    result = []
    for i in range(2):
        q = deque()
        left = i
        for log in log_list:
            if left == 1:
                q.appendleft(log)
                left = 0
            else:
                q.append(log)
                left = 1
        result.append(q)

    min_result = float('INF')

    for res in result:
        max_res = 0
        for i in range(1, len(res)):
            max_res = max(max_res, abs(res[i-1] - res[i]))
        max_res = max(max_res, abs(res[0] - res[-1]))
        min_result = min(max_res, min_result)
    print(min_result)