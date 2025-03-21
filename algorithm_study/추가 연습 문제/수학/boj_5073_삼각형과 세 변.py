data = []
while True:
    line = list(map(int, input().split()))
    if line == [0, 0, 0]:
        break
    data.append(line)

for i in range(len(data)):
    tri = []
    set_tri = set()
    select = data[i]
    for j in range(3):
        set_tri.add(select[j])
        tri.append(select[j])
    tri.sort(reverse=True)
    if tri[0] >= tri[1] + tri[2]:
        print("Invalid")
        continue
    if len(set_tri) == 1:
        print("Equilateral")
    elif len(set_tri) == 2:
        print("Isosceles")
    else:
        print("Scalene")
