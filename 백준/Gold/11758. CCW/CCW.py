x = []
y = []

for _ in range(3):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

cal1 = (x[0]*y[1]) + (x[1]*y[2]) + (x[2]*y[0])
cal2 = (y[0]*x[1]) + (y[1]*x[2]) + (y[2]*x[0])

if cal1 - cal2 > 0:
    print(1)
elif cal1 - cal2 < 0:
    print(-1)
else:
    print(0)
