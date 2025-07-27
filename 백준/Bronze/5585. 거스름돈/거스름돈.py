n = int(input())

target = 1000 - n

cnt = 0
while target > 0:
    if target >= 500:
        cnt += target // 500
        target %= 500
    elif target >= 100:
        cnt += target // 100
        target %= 100
    elif target >= 50:
        cnt += target // 50
        target %= 50
    elif target >= 10:
        cnt += target // 10
        target %= 10
    elif target >= 5:
        cnt += target // 5
        target %= 5
    elif target >= 1:
        cnt += target // 1
        target %= 1

print(cnt)