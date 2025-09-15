def solution(n, w, num):
    row = (num - 1) // w
    pos = (num - 1) % w
    col = pos if (row % 2 == 0) else (w - 1 - pos)

    last_row = (n - 1) // w
    rem = n % w

    cnt = 0
    for r in range(row, last_row + 1):
        if r < last_row or rem == 0:
            cnt += 1
        else:
            if (r % 2 == 0 and col < rem) or (r % 2 == 1 and col >= w - rem):
                cnt += 1
    return cnt
