import sys
input = sys.stdin.readline

min_val, max_val = map(int, input().split())

size = max_val - min_val + 1

is_square_free = [True] * size

i = 2
while i * i <= max_val:
    square = i * i

    start = ((min_val + square - 1) // square) * square

    for j in range(start, max_val + 1, square):
        is_square_free[j - min_val] = False

    i += 1

print(sum(is_square_free))