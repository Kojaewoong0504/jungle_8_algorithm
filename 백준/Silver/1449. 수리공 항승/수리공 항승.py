n, l = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
start_point = points[0] - 0.5
end_point = start_point + l
count = 1

for i in range(1, n):
    point = points[i]
    if point > end_point:
        start_point = point - 0.5
        end_point = start_point + l
        count += 1

print(count)