import sys
input = sys.stdin.readline

cards_num = [ 0 for i in range(10)]
cards_real_num = [ 0 for i in range(5)]
cards_color = {'R':0 , 'B':0, 'Y':0, 'G':0}

for i in range(5):
    card = list(map(str, input().split()))
    cards_color[card[0]] += 1
    cards_num[int(card[1])] += 1
    cards_real_num[i] = int(card[1])

def check_line_card(len_num):
    check = 0
    for i in range(10):
        if cards_num[i] != 0:
            check += 1
        else:
            check = 0
        if check == len_num:
            return i
    return 0
    

answer = 0
# 1
if 5 in cards_color.values() and check_line_card(5):
    answer = check_line_card(5) + 900
# 2
elif 4 in cards_num:
    answer = cards_num.index(4)+800
# 3
elif 3 in cards_num and 2 in cards_num:
    answer = (cards_num.index(3)*10)+cards_num.index(2)+700
# 4
elif 5 in cards_color.values():
    answer = max(cards_real_num)+600
# 5
elif check_line_card(5):
    answer = check_line_card(5) + 500
# 6
elif 3 in cards_num:
    answer = cards_num.index(3)+400
# 7 # 8
elif 2 in cards_num:
    num1 = cards_num.index(2)
    num2 = 0
    if 2 in cards_num[0:num1-1]:
        num2 = cards_num.index(2, 0, num1-1)
    elif 2 in cards_num[num1+1:10]:
        num2 = cards_num.index(2, num1+1, 10)
    else:
        answer = cards_num.index(2)+200
    if num2 != 0:
        answer = (max(num1, num2)*10) + min(num1, num2)+300
# 9
else:
    answer = max(cards_real_num)+100
        
print(answer)