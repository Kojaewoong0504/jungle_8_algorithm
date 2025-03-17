m = int(input())
n = int(input())

min_value = float('INF')
correct_num = []


for i in range(101):
    if m <= i*i <=n:
        correct_num.append(i*i)
        min_value = min(min_value, i*i)

if correct_num:
    print(sum(correct_num))
    print(min_value)
else:
    print(-1)