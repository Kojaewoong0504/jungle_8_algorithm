# import sys
# input = sys.stdin.readline
#
# N = int(input())
# area = [list(map(int, input().split())) for _ in range(N)]
#
# def recursion(x, y, n, area):
#     half = n // 2
#     if half == 1:
#         second_list = []
#         second_list.append(area[x][y])
#         second_list.append(area[x][y+1])
#         second_list.append(area[x+1][y])
#         second_list.append(area[x+1][y+1])
#         second_list.sort()
#         return second_list[-2]
#     else:
#         second_list = []
#         second_list.append(recursion(x, y, area, half))
#         second_list.append(recursion(x + half, y, area, half))
#         second_list.append(recursion(x, y + half, area, half))
#         second_list.append(recursion(x + half, y + half, area, half))
#         second_list.sort()
#         return second_list[-2]
#
# print(recursion(0, 0, N, area))

import sys

input=sys.stdin.readline

N=int(input())

board=[list(map(int,input().split())) for _ in range(N)]

def divide_conquer(n,board,i,j):
    side=n//2
    if side==1:
        arr=[]
        arr.append(board[i][j])
        arr.append(board[i][j+1])
        arr.append(board[i+1][j])
        arr.append(board[i+1][j+1])
        arr.sort()
        return arr[-2]
    else:
        arr=[]
        arr.append(divide_conquer(side,board,i,j))
        arr.append(divide_conquer(side,board,i+side,j))
        arr.append(divide_conquer(side,board,i,j+side))
        arr.append(divide_conquer(side,board,i+side,j+side))
        arr.sort()
        return arr[-2]
print(divide_conquer(N,board,0,0))