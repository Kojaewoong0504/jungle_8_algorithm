charge = 0  # 총 전화 요금
for _ in range(int(input())):
    s = input()
    s = s.replace(':', ' ')
    h, m, time = map(int, s.split())  # 전화 시작 시간
    end_h, end_m = h, 0  # 전화 종료 시간

    # 시간, 분이 단위를 넘어가면
    if time + m >= 60:
        end_m = time + m - 60
        end_h = h + 1
        if end_h > 23:
            end_h = 0
    else:
        end_m = time + m

    # 요금 변환 시간에 전화 중일 때
    if (end_h == 7 or end_h == 19) and m >= end_m and end_m != 0:
        # 7시를 넘기면
        if end_h == 7:
            charge += (time - end_m) * 5 + end_m * 10
        # 19시를 넘기면
        elif end_h == 19:
            charge += (time - end_m) * 10 + end_m * 5
    else:
        if 7 <= h <= 18:
            charge += time * 10
        else:
            charge += time * 5

print(charge)