d, k = map(int, input().split())

a = [0] * (d + 1)
b = [0] * (d + 1)

a[1], b[1] = 1, 0
a[2], b[2] = 0, 1
for i in range(3, d + 1):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]

for A in range(1, k + 1):
    remaining = k - A * a[d]
    if remaining % b[d] == 0:
        B = remaining // b[d]
        if A <= B:
            print(A)
            print(B)
            break
