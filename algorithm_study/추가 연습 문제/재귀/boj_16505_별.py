n = int(input())
size = 2 ** n
board = [[' ' for _ in range(size)] for _ in range(size)]


def recursion(x, y, size):
    if size == 1:
        board[x][y] = '*'
        return
    else:
        half = size // 2
        recursion(x, y, half)
        recursion(x + half, y, half)
        recursion(x, y + half, half)

recursion(0, 0, size)

for i in range(size):
    print(''.join(board[i]).rstrip())