def solution(tc, p):
    parties = []
    for _ in range(p):
        s, e = map(int, input().split())
        e -= 1 # 종료 시간을 1 감소시킴 (자바 코드와 동일하게)
        if s > e: # 시작 시간이 종료 시간보다 크면 건너뜀
            continue
    parties.append((s, e))
    parties.sort(key=lambda x: (x[0], -x[1]))

    cnt = 0
    for t in range(8, 24):  # 8시부터 23시까지
        for d in range(2):  # 각 시간대에 2번씩 확인 (30분 단위)
            for i in range(len(parties)):
                if i < len(parties):  # 인덱스 범위 체크
                    s, e = parties[i]
                    if s <= t and e >= t:  # 현재 시간에 참석 가능한 파티
                        cnt += 1
                        parties.pop(i)  # 참석한 파티 제거
                        break

    return f"On day {tc} Emma can attend as many as {cnt} parties."

day = 1
tc = 1
results = []
while True:
    p = int(input())
    if p == 0:
        break
    results.append(solution(tc, p))
    tc += 1

for result in results:
    print(result)