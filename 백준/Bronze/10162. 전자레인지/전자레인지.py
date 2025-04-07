n = int(input())

a = 300
b = 60
c = 10

result = [0,0,0]

result[0] = n // a
n = n % a

result[1] = n // b
n = n % b

result[2] = n // c
n = n % c

if n > 0:
    print(-1)
else:
    print(*result)