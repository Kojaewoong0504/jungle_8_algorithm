n = int(input())

x = [0] * (n+1)

for i in range(n+1):
    if i == 0:
        x[0] = 2
    else:
        x[i] = x[i-1] + 2**(i-1)


print(x[n]**2)
