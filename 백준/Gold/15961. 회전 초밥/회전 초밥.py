import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi_dishes = [ int(input()) for _ in range(n) ]
sushi_dishes = sushi_dishes + sushi_dishes[:k-1]
count = [0] * (d+1)

distinct = 0

for i in range(k):
    if count[sushi_dishes[i]] == 0:
        distinct += 1
    count[sushi_dishes[i]] += 1

answer = distinct + 1 if count[c] == 0 else distinct

for i in range(1, n):
    left = sushi_dishes[i - 1]
    right = sushi_dishes[i + k - 1]

    count[left] -= 1
    if count[left] == 0:
        distinct -= 1

    if count[right] == 0:
        distinct += 1
    count[right] += 1

    current = distinct + 1 if count[c] == 0 else distinct
    answer = max(answer, current)

print(answer)