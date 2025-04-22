N = int(input())

sum_data = 0
for i in range(N):
    word = input()
    word_list = list(word)
    set_word = set(word_list)
    choice = True
    for j in set_word:
        j_count = word.count(j)
        if j_count != 1:
            fr = word.find(j)
            bk = word.rfind(j)
            if bk-fr+1 != j_count:
                choice = False
                break
    if choice:
        sum_data +=1

print(sum_data)