n = int(input())
for i in range(n):
    sum_data = 0
    now_data = 0
    score = input()
    for i in score:
        if i == "O":
            now_data += 1
        else:
            now_data = 0
        sum_data += now_data
    print(sum_data)
