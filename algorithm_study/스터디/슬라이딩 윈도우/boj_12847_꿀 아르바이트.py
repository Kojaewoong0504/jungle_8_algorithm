import sys
input = sys.stdin.readline

n, m = map(int, input().split())
costs = list(map(int, input().split()))

max_cost = cal_cost = sum(costs[0:m])
for i in range(n - m):
    max_cost -= costs[i]
    max_cost += costs[i+m]
    cal_cost = max(cal_cost, max_cost)
print(cal_cost)
