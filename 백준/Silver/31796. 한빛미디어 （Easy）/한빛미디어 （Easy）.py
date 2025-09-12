n = int(input())

books = list(map(int, input().split()))

books.sort()

cnt = 1
before = books[0]
for i in range(1, n):
    if books[i] >= before * 2:
        cnt += 1
        before = books[i]

print(cnt)