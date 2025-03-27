# 입력 처리 부분
n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
needs = list(map(int, input().split()))

# 결과 저장 리스트 선언
result = [0]*m


# 이진 탐색 코드
def binary_search(target):
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return False


# 이진 탐색 호출 for 문
for i in range(m):

    # 만약 이진 탐색 결과 값이 True 라면
    if binary_search(needs[i]):
        # 결과 리스트에 해당 인덱스 값 1 증가
        result[i] = 1

# 결과 출력
print(*result)
