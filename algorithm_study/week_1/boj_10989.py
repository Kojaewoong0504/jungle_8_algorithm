# 바잔 1 : python 내장 sort 사용 - 퀵정렬이라고 알고 있다.
n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)

# 이 문제는 계수정렬을 해야 한다.!!!!!!
# 계수 정렬에 대해 알아봐야 한다.