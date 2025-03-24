t = int(input())
dp = [0] * t
for i in range(t):
    if i == 0:
        dp[0] = 1
    elif i == 1:
        dp[1] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[t-1] % 1000000)

# 메모리 최적화?
N = int(input())

mod = 1000000
fibo = [0, 1]
p = mod//10*15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod

print(fibo[N%p])