n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

# 설정된 최소 거리를 사용해 설치 가능한 최대 공유기의 개수를 구한다.
def calc_count(dist):

    # 가장 처음 설치한 공유기 정보
    past_x, cnt = houses[0], 1

    # 0번 공유기는 위에서 이미 설치 했기 때문에 제외하고 1부터 n-1까지 반복
    for i in range(1, n):

        # 다음 집의 위치와 이전 첫 공유기 설치 위치를 뺀 값을 설치 거리보다 큰지 확인
        if houses[i] - past_x >= dist:
            
            # 설치 가능하면 설치된 집의 위치 값을 past_x에 저장하고
            # 카운트 변수의 값을 증가시킨다.
            past_x = houses[i]
            cnt += 1
    return cnt

# r 값은 이론적으로 집들 사이에서 설치 가능한 최대 거리의 상한선을 설정한다.
l, r = 1, (houses[n - 1] - houses[0] // (c - 1))
while l <= r:

    # 이진 탐색 같지만 실제 리스트 내의 특정 값을 찾는 것은 아니다.
    # 이런 방식을 파라메트릭 서치라고 한다.
    mid = (l + r) // 2
    if calc_count(mid) >= c:
        l = mid + 1
    else:
        r = mid - 1
print(r)
