import sys
input = sys.stdin.readline

T = int(input().strip())
k = int(input().strip())
coins = [tuple(map(int, input().split())) for _ in range(k)]  # (p, n)

# dp[s] = 금액 s를 만드는 방법 수
dp = [0] * (T + 1)
dp[0] = 1  # 0원은 아무 동전도 안 쓰는 1가지

for p, c in coins:
    ndp = [0] * (T + 1)
    # 나머지 클래스별(0..p-1)로 한 줄씩 처리
    for r in range(p):
        # 줄에 해당하는 인덱스들: r, r+p, r+2p, ...
        idxs = list(range(r, T + 1, p))
        prev = [dp[i] for i in idxs]

        # 길이 c+1 윈도우 합을 prefix로 O(1) 계산
        prefix = [0] * (len(prev) + 1)
        for i, v in enumerate(prev, 1):
            prefix[i] = prefix[i - 1] + v

        for i, s in enumerate(idxs):
            # prev[i] + prev[i-1] + ... + prev[i-c] (음수 인덱스는 0으로 간주)
            left = max(0, i - c)
            ndp[s] = prefix[i + 1] - prefix[left]

    dp = ndp

print(dp[T])
