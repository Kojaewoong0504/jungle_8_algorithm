s = input().strip()
n = len(s)
digits = list(map(int, s))

ans = 0

for i in range(1, n):
    left = i - 1
    right = i
    sumL = 0
    sumR = 0

    while left >= 0 and right < n:
        sumL += digits[left]
        sumR += digits[right]
        if sumL == sumR:
            ans = max(ans, right - left + 1)
        left -= 1
        right += 1

print(ans)
