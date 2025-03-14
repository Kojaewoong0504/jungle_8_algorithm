n = int(input())

arr = list(map(int, input().split()))
result_data = 0
for i in arr:
    count = 0
    if i == 1:
        continue
    for j in range(2, (i//2)+1): #(i//2) + 1 을 한 이유는 소수를 찾을 때 자기 자신 까지 다 가는 것 보다. 반으로 나눠서 + 1ㄱ
        # 까지 하는 게 터 빨리 찾을 것 같다.
        if i%j == 0:
            count += 1
    if count == 0:
        result_data +=1

print(result_data)
