n = int(input())
for i in range(n):
    s = int(input())

    if s <= 1000000:
        print("NO")
        break

    isPrime = True
    smallestFactor = 0

    for j in range(2,1000000 + 1):
        if s % j == 0:
            isPrime = False
            smallestFactor = j
            break
    if isPrime or smallestFactor > 1000000:
        print("YES")
    else:
        print("NO")