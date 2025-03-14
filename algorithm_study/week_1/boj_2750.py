# 바잔 1 : python 내장 sort 사용 - 퀵정렬이라고 알고 있다.
n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)


# 추후 여러 정렬 방법을 직접 구현 해 볼 예정
