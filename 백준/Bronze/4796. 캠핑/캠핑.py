case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    q, r = divmod(v, p)
    print(f"Case {case}: {q * l + min(r, l)}")
    case += 1