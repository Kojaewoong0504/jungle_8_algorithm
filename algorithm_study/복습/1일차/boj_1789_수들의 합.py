S = int(input())
n, cnt = 1, 0
while (n*(n+1)/2) <= S:
    n += 1
    cnt += 1
print(cnt)