# 다이나믹 프로그래밍으로 수행
test_cases: int = int(input())
input_list: list = []

# 입역 저장
for _ in range(test_cases):
    # 반복문을 돌며 입력된 숫자 리스트에 저장
    input_list.append(int(input()))

# 테스트 케이스 횟수만큼 실행
for test_case in range(test_cases):
    # input_list 내에 있는 값을 꺼내 사용
    input_data = input_list[test_case]

    # DP 기록용 리스트 생성 및 초기화 1부터 n 까지 사용할 것이다.
    dp = [0] * (input_data + 1)

    # input_data 즉 입력된 n 값 까지의 계산 시작
    for i in range(1, input_data + 1):
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

    # 계산 결과 출력
    print(dp[input_data])


