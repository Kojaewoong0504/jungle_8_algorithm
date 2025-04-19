n = int(input())
input_list = []
for _ in range(n):
    input_list.append(int(input()))

for input_data in input_list:
    dp = [0] * (input_data + 1)
    for i in range(1,input_data + 1):
        if i == 0:
            print(0)
        elif i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[input_data])
