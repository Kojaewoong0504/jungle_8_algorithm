import sys

input = sys.stdin.readline

dp = [float('inf')] * 101
init_list = ['', '', 1, 7, 4, 2, 6, 8]
# 초기값 정의
for i in range(2, 8):
    dp[i] = init_list[i]

# dp 테이블 전처리 과정 
for i in range(8, 101):
    for j in range(2, i - 1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))
        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i - j]) + '0'))

# 가장 큰 값은 그리디로
# 가장 큰 값은 그냥 성냥 2개로 1을 만들어 자릿수를 크게 만들면 값이 커진다.
def find_biggest(num):
    result = '1' * (num // 2)
    if num % 2:
        result = '7' + result[1:]
    return result

# 가장 작은 값은 DP로
def find_smallist(num):
    return dp[num]


t = int(input())
for _ in range(t):
    n = int(input())
    print(find_smallist(n), find_biggest(n))
