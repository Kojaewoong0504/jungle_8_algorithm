n = int(input())

count = 0


def recursion(n, start, temp, final):
    if n == 1:
        print(f"{start} {final}")
        return

    recursion(n-1, start, final, temp)
    print(f"{start} {final}")
    recursion(n-1, temp, start, final)

print(2**n-1)
if n <= 20:
    recursion(n, 1, 2, 3)