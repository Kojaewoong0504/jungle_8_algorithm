import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t + 1):
    s1, s2, s3 = input().split()
    n1, n2 = len(s1), len(s2)

    possible = (len(s3) == n1 + n2)
    if not possible:
        print(f"Data set {tc}: no")
        continue

    dp = [False] * (n2 + 1)
    dp[0] = True

    for j in range(1, n2 + 1):
        dp[j] = dp[j - 1] and (s2[j - 1] == s3[j - 1])

    for i in range(1, n1 + 1):
        dp[0] = dp[0] and (s1[i - 1] == s3[i - 1])
        for j in range(1, n2 + 1):
            take_s1 = dp[j] and (s1[i - 1] == s3[i + j - 1])
            take_s2 = dp[j - 1] and (s2[j - 1] == s3[i + j - 1])
            dp[j] = take_s1 or take_s2

    print(f"Data set {tc}: {'yes' if dp[n2] else 'no'}")