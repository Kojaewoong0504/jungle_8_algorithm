a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
c1 = a * p
if c < p:
    c2 = b + ((p - c) * d)
else:
    c2 = b
if c1 < c2:
    print(c1)
else:
    print(c2)
