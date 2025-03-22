def solution(N, A, B, requests):
    result = []
    user_status = {} # 사용자별 상태 및 마지막 활동 시간 저장

    for time, user_id in requests:
        # 1. 모든 사용자의 현재 상태 업데이트
        for u in list(user_status.keys()):
            last_time = user_status[u]
            idle_time = time - last_time

            if idle_time >= B:  # 접속 해제 상태
                del user_status[u]  # 접속 해제된 사용자는 목록에서 제거

        # 2. 현재 요청한 사용자 처리
        user_status[user_id] = time

        # 3. 현재 채팅방 상태 계산
        active_users = 0
        for u, last_time in user_status.items():
            idle_time = time - last_time
            if idle_time < A:  # A 시간 미만이면 활성 상태
                active_users += 1

        result.append(active_users)

    return result


# 테스트
N, A, B = 5, 100, 200
requests = [[11, 1], [12, 2], [13, 1], [16, 3], [200, 1], [214, 1], [216, 1]]
print(solution(N, A, B, requests))
