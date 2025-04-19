import sys

sys.setrecursionlimit(10 ** 6)


def paint_star(LEN):
    DIV3 = LEN // 3
    if LEN == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return

    paint_star(DIV3)

    for i in range(0, LEN, DIV3):
        for j in range(0, LEN, DIV3):
            if i != DIV3 or j != DIV3:
                for k in range(DIV3):
                    g[i + k][j:j + DIV3] = g[k][:DIV3]


n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()


# 이 방법이 더 빠르다.

# def draw_stars(n):
#   if n==1:
#     return ['*']
#
#   Stars=draw_stars(n//3)
#   L=[]
#
#   for star in Stars:
#     L.append(star*3)
#   for star in Stars:
#     L.append(star+' '*(n//3)+star)
#   for star in Stars:
#     L.append(star*3)
#
#   return L
#
# N=int(input())
# print('\n'.join(draw_stars(N)))