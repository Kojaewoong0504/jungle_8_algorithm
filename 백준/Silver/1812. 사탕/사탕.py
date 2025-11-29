n = int(input())
s = 0
li = []
for i in range(n):
    li.append(int(input()))  
    s += li[i] * (-1)**i
a = s // 2

print(a)
for i in range(n-1):
    a = li[i] - a
    print(a)

