n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]:
    print(-1)
    exit()

cnt = 0
while len(boxs) > 0:
    for crane in cranes:
        for box in boxs:
            if crane >= box:
                boxs.remove(box)
                break
    cnt += 1

print(cnt)