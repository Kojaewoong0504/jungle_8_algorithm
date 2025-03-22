card = [i for i in range(1, 51)]

while True:
    input_data = int(input())
    if input_data == 0:
        break
    rabbit = input_data
    left, right = 1, 50  # 봉투 번호는 1부터 50까지

    result = []
    while left <= right:
        mid = (left + right) // 2
        result.append(mid)
        if mid == rabbit:
            print(*result)
            break
        elif mid < rabbit:
            left = mid + 1
        else:
            right = mid - 1
