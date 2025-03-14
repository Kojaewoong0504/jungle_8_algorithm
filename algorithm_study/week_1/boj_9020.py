def find_prime_number(data):
    if data == 1:
        return False
    for i in range(2, data//2 + 1 ):
        if data % i == 0:
            return False
    return True


n = int(input())


for _ in range(n):
    num = int(input())

    a = num // 2
    b = num // 2

    for _ in range(num // 2):
        if find_prime_number(a) and find_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1