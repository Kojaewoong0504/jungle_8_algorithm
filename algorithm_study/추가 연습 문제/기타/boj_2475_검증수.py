num_list = list(map(int, input().split()))

cal_list = []

for i in num_list:
    cal_list.append(i*i)

print(sum(cal_list) % 10)
