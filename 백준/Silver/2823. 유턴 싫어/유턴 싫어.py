import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

dead_end = False

for y in range(R):
    for x in range(C):
        if grid[y][x] != '.':
            continue
        deg = 0
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '.':
                deg += 1
        if deg <= 1:
            dead_end = True
            break
    if dead_end:
        break

print(1 if dead_end else 0)
