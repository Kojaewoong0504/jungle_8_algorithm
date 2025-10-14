import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for x in A:
    if x == 10:
        ans += 1

mult10 = sorted([x for x in A if x > 10 and x % 10 == 0])
others = [x for x in A if x > 10 and x % 10 != 0]

for x in mult10:
    k = x // 10
    need = k - 1                   
    if M >= need:
        ans += k                   
        M -= need
    else:
        ans += M                   
        M = 0
        break

if M > 0:
    for x in others:
        make = min(x // 10, M)    
        ans += make
        M -= make
        if M == 0:
            break

print(ans)
