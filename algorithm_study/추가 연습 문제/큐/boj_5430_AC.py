import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    func = input()
    n = int(input())
    num_list = map(int, eval(input()))
    q = deque(num_list)
    is_error = False
    is_reverse = False

    for f in func:
        if f == "R":
            is_reverse = not is_reverse
        elif f == "D":
            if not q:
                is_error = True
                break
            else:
                if is_reverse:
                    q.pop()
                else:
                    q.popleft()
    if is_error:
        print("error")
    else:
        result = "["
        if q:
            if is_reverse:
                result += ",".join(map(str, reversed(q)))
            else:
                result += ",".join(map(str, q))
        result += "]"
        print(result)
