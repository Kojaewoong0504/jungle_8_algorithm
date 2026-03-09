nums = [int(input()) for _ in range(10)]
eat = 0

for i in nums:
    eat += i
    if eat >= 100:
        if eat - 100 > 100 - (eat - i):
            eat -= i
        break
print(eat)