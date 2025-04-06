test_cases: int = int(input()) % 1000000009
input_list: list = []

# 입역 저장
for _ in range(test_cases):
    input_list.append(int(input()))

for test_case in range(test_cases):
    input_data = input_list[test_case]

    dp = [0] * (input_data % 1000000009 + 1)

    for i in range(1, input_data % 1000000009 + 1):
        if i == 0:
            print(0)
        elif i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-1]% 1000000009 + dp[i-2]% 1000000009 + dp[i-3]% 1000000009

    print(dp[input_data] % 1000000009)


