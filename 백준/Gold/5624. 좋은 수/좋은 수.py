n = int(input())
arr = list(map(int,input().split()))
 
one,two = set(),set()
dp = [False]*n
 
for i in range(n):
    a = arr[i]
    for o in one:
        if a-o in two:
            dp[i] = True
 
    one.add(a)
    for o in one:
        two.add(a+o)
 
print(sum(dp))