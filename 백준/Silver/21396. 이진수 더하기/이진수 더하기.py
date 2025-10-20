import sys
from collections import Counter
input = sys.stdin.readline
 
T = int(input())
 
for _ in range(T):
    n, x = map(int, input().split())
    numbers = Counter(list(map(int, input().split())))
 
    cnt = 0
 
    if x == 0:
        for k in numbers.keys():
            cnt += (numbers[k] * (numbers[k] - 1))
 
    else:
        for k in numbers.keys():
            cnt += (numbers[k] * numbers[x ^ k])
 
    cnt = cnt // 2
    print(cnt)