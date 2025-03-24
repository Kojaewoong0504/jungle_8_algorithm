import sys
input = sys.stdin.readline

n = int(input())
m, k = map(int, input().split())
total_people = m * k
pens = sorted(list(map(int, input().split())), reverse=True)

pen_cal = 0
cnt = 0
for pen in pens:
    if pen_cal >= total_people:
        break
    else:
        pen_cal += pen
        cnt += 1
if total_people > pen_cal:
    print("STRESS")
else:
    print(cnt)