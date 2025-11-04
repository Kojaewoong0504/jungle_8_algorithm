import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

best_gap_val = -1  # 최대화할 값 = floor(d/2)
best_x = None

for i in range(N - 1):
    d = A[i+1] - A[i]
    if d <= 1:
        continue  # 후보 없음
    val = d // 2
    x = A[i] + val  # 가운데(동률 시 더 작은 쪽)
    if val > best_gap_val or (val == best_gap_val and (best_x is None or x < best_x)):
        best_gap_val = val
        best_x = x

print(best_x if best_x is not None else -1)