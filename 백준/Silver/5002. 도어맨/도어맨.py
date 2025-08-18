import sys

input = sys.stdin.readline
x = int(input().strip())
s = list(input().strip())

w = m = 0
i = 0
n = len(s)


def ok(ch, w, m, x):
    if ch == 'W':
        w += 1
    else:
        m += 1
    return abs(m - w) <= x


while i < n:
    if ok(s[i], w, m, x):
        if s[i] == 'W':
            w += 1
        else:
            m += 1
        i += 1
        continue

    if i + 1 < n and ok(s[i + 1], w, m, x):
        s[i], s[i + 1] = s[i + 1], s[i]
        continue

    break

print(w + m)
