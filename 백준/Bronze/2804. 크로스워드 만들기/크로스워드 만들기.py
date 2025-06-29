a,b = map(str, input().split())

a = list(a)
b = list(b)

result = []

for i in a:
    if i in b :
    #겹치는 값이 있다면 겹치는 값의 인덱스를 각각 구해줍니다. 
        temp = i
        a_index = a.index(temp) 
        b_index=  b.index(temp)
        break

m = len(b)
n = len(a)

for i in range(m): #줄바꿈
    for j in range(n): #가로 출력 
        if i != b_index: #b의 인덱스 값과 다른 경우
            if j == a_index:  
            #한 줄에 글자 하나씩 출력하여 단어를 세로로 완성함
                print(b[i], end = "")
            else: #인덱스 값이 다르면 .을 출력 
                print('.', end = "")
        else: #같으면 a값을 차례로 출력 (단어가 가로로 완성)
            print(a[j], end = "")

    print("")