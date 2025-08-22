import sys

input = sys.stdin.readline
N, T = map(int, input().split())
h = list(map(int, input().split()))  # h[0] = h1 = 0

# prefix sums: pref[i] = h1 + ... + hi  (pref[0] = 0)
pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + h[i - 1]

# best_loop_prefix[r] = max_{1 <= i <= r-1} (h_i + h_{i+1}), r>=1
# (루프 수익이 음수면 안 도는 게 이득이므로 나중에 max(0, ...)로 처리)
best_loop_prefix = [0] * (N + 1)
best_loop = 0
for i in range(1, N):  # i: 1..N-1
    loop_val = h[i - 1] + h[i]
    if loop_val > best_loop:
        best_loop = loop_val
    best_loop_prefix[i + 1] = best_loop  # r=i+1일 때까지의 최댓값

ans = -10 ** 30

for r in range(1, N + 1):
    base_time = 2 * (r - 1)
    if base_time > T:
        break  # r이 커질수록 base_time 증가하므로 더 볼 필요 없음

    # 1->r (r-1분) + r->1 (r-1분) 의 행복도
    # = (h2+...+hr) + (h1+...+h_{r-1}) = pref[r] + pref[r-1] (h1=0 반영됨)
    base_gain = pref[r] + pref[r - 1]

    # 남은 시간으로 가능한 2분 루프 반복
    loops = (T - base_time) // 2
    loop_gain = max(0, best_loop_prefix[r]) * loops

    ans = max(ans, base_gain + loop_gain)

print(ans)
