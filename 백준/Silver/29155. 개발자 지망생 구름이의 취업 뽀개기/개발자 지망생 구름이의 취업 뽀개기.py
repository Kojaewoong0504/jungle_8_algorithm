n = int(input())
problems = list(map(int, input().split()))
problem_data = [list(map(int, input().split())) for _ in range(n)]

problem_data.sort(key=lambda x: (x[0], x[1]))

total_time = 0
used_levels = 0

idx = 0
for level in range(1, 6):
    cnt = problems[level-1]
    if cnt == 0:
        continue
    group = []
    while idx < n and problem_data[idx][0] == level:
        group.append(problem_data[idx][1])
        idx += 1

    chosen = group[:cnt]
    total_time += sum(chosen)

    if len(chosen) > 1:
        total_time += chosen[-1] - chosen[0]
    used_levels += 1

total_time += (used_levels - 1) * 60

print(total_time)