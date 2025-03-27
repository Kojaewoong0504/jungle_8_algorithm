# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))
#
# check_dict = defaultdict(int)
# count = 0
#
# left = 0
#
# while left < len(nums):
#     cnt = 0
#     for i in range(left, n):
#         check_dict[nums[i]] += 1
#         if check_dict[nums[i]] <= k:
#             cnt += 1
#         else:
#             count = max(count, cnt)
#             check_dict = defaultdict(int)
#             left += 1
#             break
#
# print(count)

from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

check_dict = defaultdict(int)
max_length = 0
left = 0

for right in range(n):
    check_dict[nums[right]] += 1

    # 현재 추가된 숫자가 K를 초과하면 윈도우 축소
    while check_dict[nums[right]] > k:
        check_dict[nums[left]] -= 1
        if check_dict[nums[left]] == 0:
            del check_dict[nums[left]]
        left += 1

    # 현재 윈도우 길이 갱신
    max_length = max(max_length, right - left + 1)

print(max_length)
