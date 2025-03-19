n, m = map(int, input().split())


visited = []

def recursion():
    if len(visited) == m:
        print(' '.join(map(str, visited)))
        return

    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            recursion()
            visited.pop()

recursion()