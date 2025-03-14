# 바잔 1 : python 내장 sort 사용 - 퀵정렬이라고 알고 있다.
n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)

# 이 문제는 PyPy3 로 풀어야 시간 초과가 나지 않는다.
# 또한 최대 1000000 개의 수가 들어올 수 있으니 정렬 알고리즘을 선택하는 것이 중요하다.
# 한번 정렬 알고리즘의 시간 복잡도를 자세히 공부해야 할 것 같다.