import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_block = 0


def move_left(line):
    new_line = [x for x in line if x != 0]
    result = []
    i = 0

    while i < len(new_line):
        if i + 1 < len(new_line) and new_line[i] == new_line[i + 1]:
            result.append(new_line[i] * 2)
            i += 2
        else:
            result.append(new_line[i])
            i += 1

    result += [0] * (len(line) - len(result))
    return result


def move(board, direction):
    new_board = [[0] * n for _ in range(n)]

    # 0: left
    if direction == 0:
        for r in range(n):
            new_board[r] = move_left(board[r])

    # 1: right
    elif direction == 1:
        for r in range(n):
            line = board[r][::-1]
            moved = move_left(line)[::-1]
            new_board[r] = moved

    # 2: up
    elif direction == 2:
        for c in range(n):
            line = [board[r][c] for r in range(n)]
            moved = move_left(line)
            for r in range(n):
                new_board[r][c] = moved[r]

    # 3: down
    else:
        for c in range(n):
            line = [board[r][c] for r in range(n)][::-1]
            moved = move_left(line)[::-1]
            for r in range(n):
                new_board[r][c] = moved[r]

    return new_board


def dfs(board, depth):
    global max_block

    max_block = max(max_block, max(map(max, board)))

    if depth == 5:
        return

    for direction in range(4):
        next_board = move(board, direction)
        dfs(next_board, depth + 1)


dfs(board, 0)
print(max_block)