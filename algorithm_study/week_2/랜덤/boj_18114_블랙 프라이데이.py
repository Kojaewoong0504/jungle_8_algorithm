import sys
input = sys.stdin.readline

n, c = map(int, input().split())
weights = list(map(int, input().split()))
weight_set = set(weights)  # 빠른 검색을 위한 집합

# 1개 물건으로 C를 만들 수 있는지 확인
if c in weight_set:
    print(1)
    sys.exit(0)

# 2개 물건 조합 확인
for w in weights:
    if c - w in weight_set and c - w != w:
        print(1)
        sys.exit(0)

# 3개 물건 조합 확인
for i in range(n):
    for j in range(i+1, n):
        target = c - weights[i] - weights[j]
        if target in weight_set and target != weights[i] and target != weights[j]:
            print(1)
            sys.exit(0)

print(0)
