import sys

input = sys.stdin.readline
LIMIT = 9 * (10 ** 18)


# 두 수의 최대공약수를 구하기 위한 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
logs = [tuple(map(int, input().split())) for _ in range(n)]

first_withdraw = True  # 첫 출금인지를 확인하기 위한 flag
kakao_money = 0  # 카카오 머니의 잔액
max_balance = 0  # 출금 이후에 남은 잔액 중 가장 큰 값
result = 1  # 출력할 M

for log in logs:
    amount, balance = log

    if result == -1:  # M이 존재하지 않을 경우 추가 작업을 하지 않는다
        continue

    # (1) 계좌에서 충전 후 출금해야 하는 경우
    if amount < 0 and kakao_money < -amount:
        m_value = -amount + balance - kakao_money  # 충전에 필요한 금액

        if first_withdraw:  # 처음 출금
            max_balance = balance  # 잔액을 현재 로그의 잔액으로 설정
            result = m_value  # 결괏값을 현재 로그에서 충전에 필요한 금액으로 설정
            first_withdraw = False
        else:
            result = gcd(result, m_value)  # result와 m_value의 최대 공약수
            max_balance = max(max_balance, balance)  # 이전에 기록한 가장 큰 잔액과 현재 로그 잔액 중 큰 값으로 업데이트

            if result < max_balance:  # 최대 공약수가 가장 큰 잔액보다 작을 경우는 최소 충전 단위가 존재하지 않는 경우에 해당한다.
                result = -1
            else:
                if result == 1 and balance != 0:  # M이 1인데 로그의 잔액이 0이 아닌 경우는 M이 존재하지 않는 경우에 해당한다.
                    result = -1
                else:  # result값 m_value로 갱신
                    result = min(result, LIMIT)

        kakao_money = balance  # 카카오 머니의 잔액을 balance로 설정
        continue

    # (2) 그 외의 경우에는 로그에 따라 카카오 머니 잔액에서 입금이나 출금을 했을 때 로그에 기록한 balance와 일치하는지 체크
    if kakao_money + amount != balance:
        result = -1
    else:
        kakao_money = balance

print(result)
