n = int(input())
size = list(map(int, input().split()))
t, p = map(int,input().split())

count = 0
for i in size:
    if i > 0:
        cal = i % t
        if cal == 0:
            count += (i // t)
        else:
            count += (i // t + 1)

print(count)
print(f"{n//p} {n%p}")