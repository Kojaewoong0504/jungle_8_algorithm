n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
flower_list = []

for i in flowers:
    flower_list.append([i[0]*100 + i[1], i[2]*100 + i[3]])

flower_list.sort()

end = 301
idx = 0
count = 0
last_end = 0

while end <= 1130:
    max_end = end
    while idx < len(flower_list) and flower_list[idx][0] <= end:
        max_end = max(max_end, flower_list[idx][1])
        idx += 1

    if max_end == end:
        print(0)
        break

    end = max_end
    count += 1
else:
    print(count)
