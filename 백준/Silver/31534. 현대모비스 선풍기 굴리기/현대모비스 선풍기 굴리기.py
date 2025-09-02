import math

a, b, h = map(int, input().split())

if a == b:
    print(-1)
else:
    R = max(a, b)
    r = min(a, b)
    x = R * h / (R - r)           
    area = math.pi * ((x*x + R*R) - ((x - h)*(x - h) + r*r))
    print(area)
