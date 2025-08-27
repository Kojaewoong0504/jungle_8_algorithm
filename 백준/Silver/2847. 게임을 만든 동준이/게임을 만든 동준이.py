n = int(input())

level = [int(input()) for _ in range(n)]

cnt = 0

for i in range(n-2, -1, -1):
    if level[i] < level[i+1]:
        continue
    else:
        diff = (abs(level[i+1] - level[i]) + 1)
        level[i] -= diff
        cnt += diff

print(cnt)