def checkAlpha(x):
    lst = [0] * 26
    for i in x:
        lst[ord(i) - 97] += 1

    return lst


a = checkAlpha(input())
b = checkAlpha(input())

result = 0

for i in range(26):
    if a[i] != b[i]:
        result += abs(a[i] - b[i])

print(result)
