n = int(input())
stones = list(map(int, input().split()))
operations = []

# 각 위치에 있어야 할 올바른 값 찾기
for i in range(n):
    if stones[i] == i + 1:  # 이미 올바른 위치에 있는 경우
        continue

    # i+1이 있는 위치 찾기
    for j in range(i + 1, n):
        if stones[j] == i + 1:
            # i부터 j까지 뒤집기
            operations.append((i + 1, j + 1))  # 1-indexed로 변환
            stones[i:j + 1] = stones[i:j + 1][::-1]
            break

# 연산 수가 100 이하인지 확인
if len(operations) <= 100:
    print(len(operations))
    for l, r in operations:
        print(f"{l} {r}")
else:
    print(-1)
