import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
mid = (n + 1) // 2

# 중앙값을 나누다 보면 어느 순간 앞 수들과 비교해 작아지고 그럼 순서가 바뀐다.
# 그래서 중앙값 보다 앞의 숫자들고 결국 공평하게 나누어야 한다.
ans = sum(x.bit_length() for x in nums[:mid]) - (mid - 1)

print(ans)
