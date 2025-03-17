import sys

n = int(sys.stdin.readline())

arr1 = []
arr2 = []
answer = 0

for i in range(n):
    num = (int(sys.stdin.readline()))
    if num > 1:
        arr1.append(num)
    elif num == 1:
        answer += num
    else:
        arr2.append(num)
arr1.sort(reverse = True)
arr2.sort()

for i in range(0, len(arr1), 2):
    if i + 1 < len(arr1):
        answer += arr1[i] * arr1[i + 1]
    else:
        answer += arr1[i]

for i in range(0, len(arr2), 2):
    if i + 1 < len(arr2):
        answer += arr2[i] * arr2[i + 1]
    else:
        answer += arr2[i]
print(answer)