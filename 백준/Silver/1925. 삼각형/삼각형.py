# 입력
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def sqdist(ax, ay, bx, by):
    dx = ax - bx
    dy = ay - by
    return dx*dx + dy*dy

# 세 점이 일직선인지: (B - A) x (C - A) == 0
cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
if cross == 0:
    print("X")
    exit()

# 세 변의 제곱길이
ab = sqdist(x1, y1, x2, y2)
bc = sqdist(x2, y2, x3, y3)
ca = sqdist(x3, y3, x1, y1)

# 가장 긴 변이 마지막에 오도록 정렬: a <= b <= c
a, b, c = sorted([ab, bc, ca])

# 정삼각형?
if a == b == c:
    print("JungTriangle")
    exit()

# 이등변 여부 (정삼각형은 이미 처리)
is_isosceles = (a == b) or (b == c) or (a == c)

# 각의 종류 (제곱길이로 판정)
# a + b ? c
if a + b < c:
    angle = "Dunkak"      # 둔각
elif a + b == c:
    angle = "Jikkak"      # 직각
else:
    angle = "Yeahkak"     # 예각

# 출력 조립
if is_isosceles:
    print(angle + "2Triangle")
else:
    print(angle + "Triangle")
