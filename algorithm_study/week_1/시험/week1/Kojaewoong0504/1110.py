# 숫자 n 입력
input_num: int = int(input())


# 새로운 숫자를 만드는 함수
def trans_num(old_num: int) -> int:
    # 이전 값이 10보다 작은 경우
    if old_num < 10:
        right_num: int = old_num
        new_num: int = old_num
        return right_num * 10 + new_num
    # 이전 값이 10보다 큰 경우
    else:
        right_num: int = old_num % 10
        new_num: int = (old_num // 10) + (old_num % 10)
        return (right_num * 10) + (new_num % 10)

# 입력 값을 계속 변경할 예정이니 최초 값을 저장한다.
first_data: int = input_num
# 카운트 변수
cnt: int = 0

# 반복문 수행
while True:
    # 조건에 맞게 숫자를 변형하고 그 값을 저장한다.
    new_data: int = trans_num(input_num)

    # 새로 생성한 겂이 최초의 값과 같아질 경우
    if first_data == new_data:
        # 카운트 증가 후 반복문 탈출
        cnt += 1
        break
    # 생성한 값이 최초 값과 다른 경우 카운트 증가 후 계속 반복
    else:
        cnt += 1
        input_num = new_data

print(cnt)
