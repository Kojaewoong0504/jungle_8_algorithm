N,M = map(int,input().split())
s = []

def recursion(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            recursion(i+1)
            s.pop()

recursion(1)
