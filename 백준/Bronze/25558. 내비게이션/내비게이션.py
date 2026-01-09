n = int(input())
sx, sy, ex, ey = map(int, input().split())
lst = []
 
for _ in range(n) :
    result = 0
    tsx, tsy, tex, tey = sx, sy, ex, ey
    for _ in range(int(input())) :
        x, y = map(int, input().split())
        result += abs(tsx-x) + abs(tsy-y)
        tsx, tsy = x, y
    result += abs(tsx-tex) + abs(tsy-tey)
    lst.append(result)
 
print(lst.index(min(lst))+1)