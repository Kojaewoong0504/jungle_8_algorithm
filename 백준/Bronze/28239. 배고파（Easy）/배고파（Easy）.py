n = int(input())

for _ in range(n):
    m = int(input())

    bits = []
    for i in range(60):
        if m & (1 << i):
            bits.append(i)

    if len(bits) == 1:
        print(bits[0] - 1, bits[0] - 1)
    else:
        print(bits[0], bits[1])
