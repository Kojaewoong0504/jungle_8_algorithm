n = int(input())

def cording_festival_1(score):
    if score > 100:
        return 0
    if score == 1:
        return 5000000
    elif 1 < score <= 3:
        return 3000000
    elif 3 < score <= 6:
        return 2000000
    elif 6 < score <= 10:
        return 500000
    elif 10 < score <= 15:
        return 300000
    elif 15 < score <= 21:
        return 100000
    else:
        return 0

def cording_festival_2(score):
    if score > 64:
        return 0
    if score == 1:
        return 5120000
    elif 1 < score <= 3:
        return 2560000
    elif 3 < score <= 7:
        return 1280000
    elif 7 < score <= 15:
        return 640000
    elif 15 < score <= 31:
        return 320000
    else:
        return 0

for _ in range(n):
    scores = list(map(int, input().split()))
    print(cording_festival_1(scores[0]) + cording_festival_2(scores[1]))