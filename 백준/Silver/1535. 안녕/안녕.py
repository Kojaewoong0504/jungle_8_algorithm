import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

# dp[w] = 총 잃은 체력이 w일 때의 최대 기쁨 (w = 0..99)
dp = [0] * 100  # 용량 99까지만 유효

for l, j in zip(L, J):
    # 같은 사람을 중복 사용하지 않도록 뒤에서 앞으로
    for w in range(99, -1, -1):
        if w + l < 100:  # 총 잃는 체력이 99 이하여야 함
            dp[w + l] = max(dp[w + l], dp[w] + j)

print(max(dp))
