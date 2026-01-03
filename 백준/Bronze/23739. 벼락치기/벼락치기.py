N = int(input())
time = 30
chap = 0

while (N > 0) :
    time = 30
    while (time > 0) and (N > 0):
        T = int(input())

        if (time / T) >= (1 / 2) or (time >= T):
            chap += 1
            time -= T
            N -= 1
        else :
            time -= T
            N -= 1
print(chap)