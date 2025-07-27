n, k = map(int, input().split())
placement = list(input())
ans = 0
for i in range(n):
    if placement[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if placement[j] == 'H':
                placement[j] = 0
                ans += 1
                break
print(ans)