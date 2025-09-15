import sys

def mmss(sec: int) -> str:
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"

input = sys.stdin.readline

N = int(input())
events = []
for _ in range(N):
    team, t = input().split()
    mm, ss = map(int, t.split(':'))
    events.append((int(team), mm * 60 + ss))

events.sort(key=lambda x: x[1])

score1 = score2 = 0
lead1 = lead2 = 0
last = 0
END = 48 * 60

for team, cur in events:
    if score1 > score2:
        lead1 += cur - last
    elif score2 > score1:
        lead2 += cur - last

    if team == 1:
        score1 += 1
    else:
        score2 += 1

    last = cur

if score1 > score2:
    lead1 += END - last
elif score2 > score1:
    lead2 += END - last

print(mmss(lead1))
print(mmss(lead2))
