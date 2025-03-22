from itertools import combinations


def solution(fruits, k):
    n = len(fruits)

    # 모든 과일 조합 생성
    fruit_combinations = list(combinations(range(n), k))

    # 각 조합별 맛 계산
    unique_tastes = set()

    for combo in fruit_combinations:
        # 초기 맛 조합 (모두 0)
        taste_combination = ['0'] * len(fruits[0])

        # 선택한 과일들의 맛 합치기 (OR 연산)
        for fruit_idx in combo:
            for i in range(len(taste_combination)):
                if fruits[fruit_idx][i] == '1':
                    taste_combination[i] = '1'

        # 맛 조합을 문자열로 변환하여 set에 추가
        unique_tastes.add(''.join(taste_combination))

    return len(unique_tastes)


# 예제 테스트
fruits = ["1100", "0110", "0011", "1100"]
k = 2
print(solution(fruits, k))  # 출력: 4
