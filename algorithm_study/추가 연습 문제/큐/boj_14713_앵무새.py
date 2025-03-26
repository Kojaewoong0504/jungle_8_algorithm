from collections import deque

n = int(input())
word_list = [input().split() for _ in range(n)]
long_word = input().split()
q = deque(long_word)

possible = True
while q and possible:
    word = q.popleft()
    found = False
    for i in range(n):
        if word_list[i] and word_list[i][0] == word:
            word_list[i].pop(0)
            found = True
            break
    if not found:
        possible = False

# 모든 앵무새의 문장이 비어있는지 확인
for words in word_list:
    if words:
        possible = False
        break

print("Possible" if possible else "Impossible")
