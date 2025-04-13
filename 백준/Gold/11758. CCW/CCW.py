x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)


cal1 = (x_list[0] * y_list[1] + x_list[1] * y_list[2] + x_list[2] * y_list[0])
cal2 = (y_list[0] * x_list[1] + y_list[1] * x_list[2] + y_list[2] * x_list[0])

if cal1 - cal2 > 0:
    print(1)
elif cal1 - cal2 < 0:
    print(-1)
else:
    print(0)