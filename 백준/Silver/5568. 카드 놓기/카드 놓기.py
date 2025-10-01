from itertools import permutations

n = int(input())
k = int(input())

nums = list(int(input()) for _ in range(n))

data = set()
for p in permutations(nums, k):
    str_data = ""
    for num in p:
        str_data += str(num)
    data.add(int(str_data))

print(len(data))