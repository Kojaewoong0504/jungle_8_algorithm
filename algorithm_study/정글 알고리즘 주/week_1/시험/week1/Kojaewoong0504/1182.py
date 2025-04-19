# 재귀 사용

n, s = map(int, input().split())
arr: list = list(map(int, input().split()))

# 생성한 수열을 기록할 리스트 선언
memory: list = []
# 부분수열의 횟수를 기록하기 위한 변수 선언
count: int = 0

# 재귀 함수
def recursion(start):
    global count

    # 재귀 탈출 조건이 따로 없다. 모든 경로를 탐색할 것이다.
    # 대신 부분수열의 개수를 체크하기 위한 조건문 사용
    if len(memory) > 0 and sum(memory) == s:
        count += 1

    # 재귀 호출 마다 for문을 사용한다. 재귀에 진입할 때 마다
    # for문의 시작 값이 커지며 이전에 입력된 값을 제외 하여 중복을 피한다.
    # 재귀를 돌면 서 수열의 크기가 점점 줄어들 것이다.
    for i in range(start, n):
        # 선택된 값을 메모리 리스트에 저장
        memory.append(arr[i])
        # 재귀 실행
        recursion(i+1)
        # 재귀에서 반환되면 메모리에 있던 값을 제거한다.
        memory.pop()

    #최종 부분수열 탐색 결과 반환
    return count

print(recursion(0))