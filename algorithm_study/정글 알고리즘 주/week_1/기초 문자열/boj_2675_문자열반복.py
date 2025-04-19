t = int(input())

for i in range(t):
    num, word = map(str, input().split())
    for j in word:
        print(j * int(num), end="")
    print("")