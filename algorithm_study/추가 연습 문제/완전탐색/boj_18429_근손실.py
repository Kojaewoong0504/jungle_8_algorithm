from itertools import permutations
import sys
input=sys.stdin.readline
N,K=map(int, input().split())
A = list(map(int, input().split()))
cnt=0
for i in permutations(A, N):
    w=500
    for j in i:
        w+=j-K
        if w<500: break
    if w>=500: cnt+=1            
print(cnt)