import sys
input = sys.stdin.readline

n = int(input())
if n < 2023: #2023보다 작은 경우 0개 가능. 사실 없어도 상관 없는 조건문이다. 
    print(0)
else:
    ans = 0
    for i in range(2023, n + 1):
        x = str(i)
        if not {'2', '3', '0'}.issubset(set(x)): #0, 2, 3 원소가 문자열에 있는지 확인
            continue
        tmp = []
        for j in x: #2023이 있다면 하나씩 추가하며 당첨 티켓을 만들 수 있는지 확인. 
            if j == '2' and len(tmp) in [0, 2]:
                tmp.append(j)
            elif j == '0' and len(tmp) == 1:
                tmp.append(j)
            elif j =='3' and len(tmp) == 3:
                ans += 1 #완성하면 1 추가
                break
    print(ans)