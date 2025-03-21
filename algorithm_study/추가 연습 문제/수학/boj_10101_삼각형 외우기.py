tri = []
set_tri = set()
for _ in range(3):
    data = int(input())
    set_tri.add(data)
    tri.append(data)

if sum(tri) == 180:
    if len(set_tri) == 1:
        print("Equilateral")
    elif len(set_tri) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")


