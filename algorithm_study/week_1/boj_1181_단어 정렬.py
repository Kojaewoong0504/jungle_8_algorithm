n = int(input())

word_list = []

for _ in range(n):
    word_list.append(input())

set_word = list(set(word_list))
sort_word = sorted(set_word, key= lambda x : (len(x), x))

for w in sort_word:
    print(w)

# 이 문제는 파이썬 lambda 식을 사용해야 한다.