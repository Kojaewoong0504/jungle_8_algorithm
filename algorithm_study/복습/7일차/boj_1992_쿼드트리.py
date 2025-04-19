n = int(input())

screen = [list(input()[:]) for _ in range(n)]

def check_same_num(x, y, n, bw):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if screen[i][j] != bw:
                return False
    return True


def recursion(x, y, n):
    if check_same_num(x, y, n, screen[x][y]):
        return screen[x][y]
    else:
        half = n//2
        temp = "("
        temp += recursion(x, y, half)
        temp += recursion(x, y+half, half)
        temp += recursion(x+half, y, half)
        temp += recursion(x+half, y+half, half)
        temp += ")"
    return temp

print(recursion(0, 0, n))