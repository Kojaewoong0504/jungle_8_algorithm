m, n = map(int, input().split())

n_length = list(map(int, input().split()))

left = 1
right = max(n_length)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    count = 0
    for length in n_length:
        count += length // mid
    
    if count >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
    