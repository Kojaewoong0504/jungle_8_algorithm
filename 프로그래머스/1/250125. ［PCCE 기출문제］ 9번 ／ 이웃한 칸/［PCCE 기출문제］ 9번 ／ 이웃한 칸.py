def solution(board, h, w):
    n = len(board)
    color = board[h][w]
    count = 0
    # 우, 하, 상, 좌
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0 <= nh < n and 0 <= nw < n and board[nh][nw] == color:
            count += 1

    return count