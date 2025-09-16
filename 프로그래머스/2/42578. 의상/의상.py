from collections import Counter

def solution(clothes):
    # 종류별 개수 세기
    kind_count = Counter(kind for _, kind in clothes)
    # 각 종류에서 (입지 않음 포함) 경우의 수를 곱하고, 모두 안 입음 1가지를 제외
    ans = 1
    for cnt in kind_count.values():
        ans *= (cnt + 1)
    return ans - 1
