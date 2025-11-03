num = int(input())
vel = list(map(int,input().split()))
count = 1
result = 0
for i in range(num-1,-1,-1):
    if count <= vel[i]:
        result += count
        count += 1
    else:
        result += vel[i]
        count = vel[i] + 1
        
print(result)