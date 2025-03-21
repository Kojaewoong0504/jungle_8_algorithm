n = int(input())

x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_max = max(x_list)
y_max = max(y_list)
x_min = min(x_list)
y_min = min(y_list)

print(abs(x_max-x_min) * abs(y_max - y_min))