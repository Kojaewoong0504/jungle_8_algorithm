from bisect import bisect_left, bisect_right

n = int(input())

card_list = sorted(list(map(int, input().split())))

m = int(input())

target_list = list(map(int, input().split()))

result = []
for i in range(m):
    left = bisect_left(card_list, target_list[i])
    right = bisect_right(card_list, target_list[i])

    if left == right:
        result.append(0)
    else:
        result.append(right - left)

print(*result)