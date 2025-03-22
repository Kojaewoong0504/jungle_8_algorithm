def find_kth_character(k):
    # k는 1부터 시작하므로 0부터 시작하는 인덱스로 변환
    k = k - 1

    # k의 이진 표현에서 1의 개수 세기
    count = bin(k).count('1')

    # 1의 개수가 짝수면 0, 홀수면 1 반환
    return "0" if count % 2 == 0 else "1"


k = int(input())
print(find_kth_character(k))
