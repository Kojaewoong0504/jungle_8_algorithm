x, y, m = map(int, input().split())
damage = [int(input()) for _ in range(x)]
heal = [int(input()) for _ in range(y)]

if m + sum(heal) <= sum(damage):
    print(0)
    exit(0)
ans = []
max_M = m
d_idx, h_idx = 0, 0
for _ in range(x + y):
    if m > max_M // 2 and len(damage) > 0:
        m -= damage[d_idx]
        d_idx += 1
        ans.append(-d_idx)
    elif m <= max_M // 2 and len(heal) > 0:
        m += heal[h_idx]
        h_idx += 1
        ans.append(h_idx)

    if d_idx == len(damage) and h_idx != len(heal):
        while h_idx < len(heal):
            m += heal[h_idx]
            h_idx += 1
            ans.append(h_idx)
        break
print('\n'.join(map(str, ans)) if len(ans) == x + y else 0)
