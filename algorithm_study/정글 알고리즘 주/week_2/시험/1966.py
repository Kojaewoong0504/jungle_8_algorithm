# 사용 라이브러리 선언 부
from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 입력
t = int(input())

# 테스트 케이스 수 만큼 반복
for _ in range(t):

    # 입력 처리 부
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # 큐 선언 및 초기화
    q = deque(data)

    # 결과 갯수 카운트 변수 선언
    result = 1

    # 큐안에 데이터가 없을 때까지 반복
    while q:

        # 큐에서 가장 먼저 나올 데이터가 중요도가 가장 높은지 확인
        if q[0] < max(q):
            # 중요도가 가장 높은 데이터가 아닐 경우
            # 큐의 제일 뒤에 데이터를 다시 넣는다.
            q.append(q.popleft())
        # 큐에서 가장 중요도가 높은 데이터인 경우
        else:
            # 만약 가장 첫번째로 출력된 문서를 보고 싶을 때 (0번을 첫번째라고 함)
            # 바로 break 후 1을 출력하고 끝낸다
            if m == 0:
                break
            # 그렇지 않을 경우 차례로 큐에서 내보내고 result 값을 1씩 증가
            q.popleft()
            result += 1

        # 큐에서 찾고자 하는 문서의 수를 추적하기 위한 코드
        if m > 0:
            m = m-1
        else:
            m = len(q)-1
    # 출력 부
    print(result)