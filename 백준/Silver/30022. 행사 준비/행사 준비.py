import sys

input = sys.stdin.readline

N, A, B = map(int, input().split())
items = []

for _ in range(N):
    p, q = map(int, input().split())
    items.append((p, q))

# 차이(abs(p-q))가 큰 순서대로 정렬
items.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

total = 0
cnt_a = 0  # 동하(상점1) 선택 수
cnt_b = 0  # 지원(상점2) 선택 수

for p, q in items:
    # 동하/지원 중 남은 수가 더 많거나, 가격이 작은 쪽이 할당받음
    if (cnt_a < A and (cnt_b == B or p < q)):
        total += p
        cnt_a += 1
    else:
        total += q
        cnt_b += 1

print(total)
