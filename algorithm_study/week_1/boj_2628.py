x, y = map(int, input().split())
n = int(input())

cut_x = [0, x]
cut_y = [0, y]

for _ in range(n):
    d, c = map(int, input().split())
    if d == 0:
        cut_y.append(c)
    else:
        cut_x.append(c)
cut_x.sort()
cut_y.sort()

max_x = 0
max_y = 0
prev_x = []
prev_y = []
for i in cut_x:
    prev_x.append(i-max_x)
    max_x = i
for i in cut_y:
    prev_y.append(i-max_y)
    max_y = i

print(max(prev_y) * max(prev_x))


