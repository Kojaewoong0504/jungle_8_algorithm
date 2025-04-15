import sys
sys.setrecursionlimit(10**8)


n, m = map(int,input().split())

choice = [False] * (n+1)
mem = []

def recursion(n, depth):
    if depth == 0:
        print(' '.join(map(str, mem)))
        return

    for i in range(1, n+1):
        if not choice[i]:
            choice[i] = True
            mem.append(i)
            recursion(n, depth-1)
            choice[i] = False
            mem.pop()


recursion(n, m)