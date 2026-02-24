n = int(input())

sec = 0
count = 1

while n > 0:
    if n >= count:
        n -= count
        count += 1
        sec += 1
    else:
        count = 1

print(sec)