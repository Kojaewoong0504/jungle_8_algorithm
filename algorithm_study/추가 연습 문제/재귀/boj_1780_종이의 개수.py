import sys
input = sys.stdin.readline

num = int(input())
paper = [list(map(int, input().split())) for _ in range(num)]

def check_same_paper(x, y, n, data):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != data:
                return False
    return True

zero_count = 0
one_count = 0
minus_one_count = 0


def recursion(x, y, n):
    global zero_count, one_count, minus_one_count
    if check_same_paper(x,y,n,paper[x][y]):
        if paper[x][y] == 0:
            zero_count += 1
        elif paper[x][y] == 1:
            one_count += 1
        else:
            minus_one_count += 1
    else:
        three = n//3
        d_three = three + three
        recursion(x, y, three)
        recursion(x + three, y, three)
        recursion(x + d_three, y, three)
        recursion(x, y + three, three)
        recursion(x + three, y + three, three)
        recursion(x + d_three, y + three, three)
        recursion(x, y + d_three, three)
        recursion(x + three, y + d_three, three)
        recursion(x + d_three, y + d_three, three)

recursion(0,0, num)
print(minus_one_count)
print(zero_count)
print(one_count)