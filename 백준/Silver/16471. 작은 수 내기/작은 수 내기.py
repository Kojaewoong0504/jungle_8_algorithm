n = int(input())
me = list(map(int, input().split()))
other = list(map(int, input().split()))

me.sort(reverse=True)
other.sort()
cnt = 0

for i in me:
    if i >= other[-1]:
        pass
    else:
        cnt += 1
        other.pop()

if cnt >= (n+1)/2:
    print("YES")
else:
    print("NO")