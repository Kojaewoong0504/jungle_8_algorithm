import math

n = int(input())

factorial_data = list(str(math.factorial(n))[:])

zero_count = 0
for i in range((len(factorial_data)-1), -1, -1):
    if factorial_data[i] == "0":
        zero_count += 1
    else:
        if zero_count > 0:
            if factorial_data[i] != "0":
                break
            else:
                zero_count += 1

print(zero_count)