import bisect

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

closest_sum = float('inf')
result_pair = None

for i in range(n):
    # 현재 용액과 합쳐서 0이 되는 이상적인 값
    target = -solutions[i]

    # bisect로 target에 가장 가까운 위치 찾기
    pos = bisect.bisect_left(solutions, target)

    # 자기 자신을 제외한 후보 위치들 확인
    candidates = []
    if pos < n and pos != i:
        candidates.append(pos)
    if pos > 0 and pos - 1 != i:
        candidates.append(pos - 1)

    # 각 후보 위치에 대해 합의 절대값 확인
    for j in candidates:
        current_sum = abs(solutions[i] + solutions[j])
        if current_sum < closest_sum:
            closest_sum = current_sum
            result_pair = (min(solutions[i], solutions[j]), max(solutions[i], solutions[j]))

print(result_pair[0], result_pair[1])
