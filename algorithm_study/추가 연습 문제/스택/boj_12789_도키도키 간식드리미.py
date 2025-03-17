n = int(input())

waiting_line = list(map(int, input().split()))
side_space = []
target = 1
possible = True


while waiting_line or side_space:
    if waiting_line and waiting_line[0] == target:
        waiting_line.pop(0)
        target += 1
    elif side_space and side_space[-1] == target:
        side_space.pop()
        target += 1
    elif waiting_line:
        side_space.append(waiting_line.pop(0))
    else:
        possible = False
        break

if possible:
    print("Nice")
else:
    print("Sad")