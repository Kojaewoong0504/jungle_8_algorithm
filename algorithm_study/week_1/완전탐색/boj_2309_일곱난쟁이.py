import sys
from itertools import combinations
input = sys.stdin.readline

short = [int(input()) for _ in range(9)]

# for i in combinations(short, 7):
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break


# 파이썬 itertools의 permutaion 이나 combinations로 문제를 풀었다.
# 하지만 추 후 이런 툴을 사용하지 못하도록 할 수 있으니 재귀를 이용해 만드는 방법도 학습해 두자.


comb_list = [-1] * 7
comb = []
def combinations_impl(n, start ,depth):
    # 탈출 조건 = 모든 난쟁이가 선택되었을 때
    if depth == 7 or start > n:
        comb.append(comb_list.copy())
        return

    for i in range(start, n):
        if comb_list[depth] == -1:
            comb_list[depth] = short[i]
            combinations_impl(n, i+1, depth+1)
            comb_list[depth] = -1

combinations_impl(9, 0, 0)

for combination in comb:
    if sum(combination) == 100:
        for i in sorted(combination):
            print(i)
        break