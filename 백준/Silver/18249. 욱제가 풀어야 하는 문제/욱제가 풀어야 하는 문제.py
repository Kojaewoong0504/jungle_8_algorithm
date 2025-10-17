import sys
MOD = 10**9 + 7
input = sys.stdin.readline

T = int(input())
Ns = [int(input()) for _ in range(T)]
maxN = max(Ns) if Ns else 0

# Fib[0]=0, Fib[1]=1 로 두고 Fib[k] = Fib[k-1]+Fib[k-2]
Fib = [0]*(maxN+2+1)  # 필요 최대: N+1 까지 => 인덱스 여유 있게
Fib[1] = 1
for k in range(2, maxN+2):
    Fib[k] = (Fib[k-1] + Fib[k-2]) % MOD

# 정답 f(N) = Fib[N+1]
out = []
for N in Ns:
    out.append(str(Fib[N+1] % MOD))
print("\n".join(out))
