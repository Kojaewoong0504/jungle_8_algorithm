# 내가 푼 방법
from collections import deque

n, k = map(int, input().split())

q = deque()
store = [i for i in range(1, n+1)]
cnt = 1
index = 0
while store:
    if cnt == k:
        q.append(store[index])
        store.pop(index)
        n -= 1
        cnt = 1
    else:
        index += 1
        cnt += 1
        if index >= n:
            index = index % n

print("<", end="")
print(", ".join(map(str, q)), end="")
print(">")

# from collections import deque
#
# n, k = map(int, input().split())
#
# q = deque([i for i in range(1, n+1)])
# result = []
#
# while q:
#     # k-1번 회전 (첫 번째 원소를 맨 뒤로 보냄)
#     for _ in range(k-1):
#         q.append(q.popleft())
#     # k번째 원소 제거 및 결과에 추가
#     result.append(q.popleft())
#
# # 요세푸스 순열 출력
# print("<", end="")
# print(", ".join(map(str, result)), end="")
# print(">")
