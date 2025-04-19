s = int(input())
n, cnt = 1, 0

while (n*(n+1)/2) <= s:
    n += 1
    cnt += 1
print(cnt)