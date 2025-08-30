import sys
input = sys.stdin.readline

def is_leap(y: int) -> bool:
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def days_since_0001_01_01(y: int, m: int, d: int) -> int:
    y_minus_1 = y - 1
    days = 365 * y_minus_1 + (y_minus_1 // 4) - (y_minus_1 // 100) + (y_minus_1 // 400)

    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        mdays[1] = 29

    for mm in range(1, m):
        days += mdays[mm - 1]

    days += (d - 1)
    return days

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if (y2 > y1 + 1000) or (y2 == y1 + 1000 and (m2 > m1 or (m2 == m1 and d2 >= d1))):
    print("gg")
    exit()

a = days_since_0001_01_01(y1, m1, d1)
b = days_since_0001_01_01(y2, m2, d2)

diff = b - a
print(f"D-{diff}")
