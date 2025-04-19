from bisect import bisect_left, bisect_right

n = int(input())
card1 = sorted(list(map(int, input().split())))
m = int(input())
card2 = list(map(int, input().split()))

result = [0] * m

for i in range(m):
    left = bisect_left(card1, card2[i])
    right = bisect_right(card1, card2[i])

    result[i] = right - left

print(*result)