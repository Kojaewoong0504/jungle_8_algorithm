n = input()
is_true = 0
for i in range(1, len(n)):
    s1, s2 = n[:i], n[i:]
    m1 = m2 = 1
    for n in s1:
        m1 *= int(n)
    for n in s2:
        m2 *= int(n)
    if m1 == m2:
        is_true = 1
        break
print("YES" if is_true else "NO")