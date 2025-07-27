k = int(input())

size = 1
while size < k:
    size *= 2
cnt = 0
result = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        cnt += 1
print(result, cnt)