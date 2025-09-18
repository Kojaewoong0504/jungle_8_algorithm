import sys
input = sys.stdin.readline

n = int(input())
seen = set()
ans = 0

for _ in range(n):
    s = input().strip()   
    if s == "ENTER":
        seen.clear()      
    else:
        if s not in seen: 
            ans += 1
            seen.add(s)

print(ans)
