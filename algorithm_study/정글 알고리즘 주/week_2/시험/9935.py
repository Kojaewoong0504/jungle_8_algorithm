# 더 빠른 입력을 위한 sys 라이브러리 선언
import sys
input = sys.stdin.readline

# 입력 처리 부
word = input().rstrip()
explosion_string = input().rstrip()

# 사용 변수 초기화 부
stack = []

# 입력 받은 폭발 문자열 개수
bomb_len = len(explosion_string)

# 문자열 길이 만큼 반복
for i in range(len(word)):
    # 스택에 문자 하나씩 추가
    stack.append(word[i])

    # 만약 스택에서 폭발문자열 길이만큼 뒤에서 뽑은 문자가 폭발 문자와 같다면
    if ''.join(stack[-bomb_len:]) == explosion_string:
        # 폭발 문자열 길이만큼 반복하며
        for _ in range(bomb_len):
            # 스택에서 제거 한다.
            stack.pop()

# 스택에 문자열이 남아있다면
if stack:
    # 남은 문자열 출력
    print(''.join(stack))
# 모든 문자열이 폭발로 사라졌다면
else:
    # FRULA 출력
    print('FRULA')