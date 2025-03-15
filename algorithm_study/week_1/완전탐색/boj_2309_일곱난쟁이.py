import sys
from itertools import combinations
input = sys.stdin.readline

short = [int(input()) for _ in range(9)]

for i in combinations(short, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break


# 파이썬 itertools의 permutaion 이나 combinations로 문제를 풀었다.
# 하지만 추 후 이런 툴을 사용하지 못하도록 할 수 있으니 재귀를 이용해 만드는 방법도 학습해 두자.