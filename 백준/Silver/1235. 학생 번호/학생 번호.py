n = int(input())
nums = [input().strip() for _ in range(n)]

L = len(nums[0])  # 번호 길이
for k in range(1, L + 1):
    suffixes = {num[-k:] for num in nums}
    if len(suffixes) == n:
        print(k)
        break
