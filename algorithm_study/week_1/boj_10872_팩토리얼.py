n = int(input())


def recursion(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    return n * recursion(n-1)


print(recursion(n))