def recursion(depth):
    if depth == 0:
        return "-"

    return recursion(depth-1) + (" "*(3**(depth-1))) + recursion(depth-1)

while True:
    try:
        n = int(input())
        print(recursion(n))
    except EOFError:
        break
    except ValueError:
        break
