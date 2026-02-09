import sys
input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(input())

# 약수를 구하는 함수
# 약수가 모두 들어가있는 list를 반환한다.
def function(x):
    mylist = []
    for i in range(1,x+1):
        if x % i == 0:
            mylist.append(i)
    return mylist

# for문을 돌리자
for i in range(T):
    number = int(input())  # 숫자를 받고
    listlist = function(number)  # 약수 list
    TF = True
    # 마지막 숫자, 즉 자기 자신이 과잉수가 아니면 'BOJ 2022'를 print하고 stop
    if sum(function(listlist[-1]))-listlist[-1] <= listlist[-1]:
        print('BOJ 2022')
        TF = False
    # 마지막 숫자, 즉 자기 자신이 과잉수면 나머지 약수를 탐색한다.
    else:
        for j in range(len(listlist)-1):
            # 자기 자신을 제외한 나머지 약수 중 과잉수가 발견되면 'BOJ 2022'를 print하고 stop
            if sum(function(listlist[j]))-listlist[j] > listlist[j]:
                print('BOJ 2022')
                TF = False
                break
        # 그동안 stop되지 않고 잘 진행되었다면 'Good Bye'를 print
        if TF:
                print('Good Bye')