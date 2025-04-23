n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()


init_start = lines[0][0]
init_end = lines[0][1]
line_len = 0
for i in range(1, len(lines)):
    if lines[i][0] <= init_end and lines[i][1] <= init_end:
        continue
    elif lines[i][0] <= init_end and lines[i][1] > init_end:
        init_end = lines[i][1]
    else:
        line_len += init_end - init_start
        init_start = lines[i][0]
        init_end = lines[i][1]
line_len += init_end - init_start

print(line_len)