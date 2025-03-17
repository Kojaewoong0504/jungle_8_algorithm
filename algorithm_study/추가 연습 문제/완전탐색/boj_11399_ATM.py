n = int(input())

arr = list(map(int, input().split()))

arr.sort()

sum_val = 0
for i in range(len(arr)+1):
    prev_val = sum(arr[0:i])
    sum_val += prev_val

print(sum_val)