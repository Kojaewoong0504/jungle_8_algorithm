n = int(input())

costs = []

for _ in range(n):
    costs.append(int(input()))

result = []

for cost in costs:
    give_back = [0] * 4
    cal_cost = cost
    while cal_cost > 0:
        if cal_cost // 25 > 0:
            give_back[0] = cal_cost // 25
            cal_cost = cal_cost % 25
        elif cal_cost // 10 > 0:
            give_back[1] = cal_cost // 10
            cal_cost = cal_cost % 10
        elif cal_cost // 5 > 0:
            give_back[2] = cal_cost // 5
            cal_cost = cal_cost % 5
        else:
            give_back[3] = cal_cost // 1
            cal_cost = 0
    result.append(give_back)

for i in range(n):
    print(' '.join(map(str, result[i])))
