# n, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# visited = [False] * k
# checked = [-1] * k
# max_result = -float('INF')
#
# def recursion(depth):
#     global max_result
#     if depth == k:
#         cal_data = int(''.join(map(str, checked)))
#         if cal_data <= n:
#             max_result = max(max_result, cal_data)
#         return
#
#     for i in range(k):
#         if i not in checked:
#             checked[depth] = data[i]
#             visited[depth] = True
#             recursion(depth + 1)
#             visited[depth] = False
#             checked[depth] = -1
#     return max_result
#
# recursion(0)
#
# print(max_result)

n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)  # 내림차순 정렬

max_result = 0

def recursion(current_num):
    global max_result

    # 현재 숫자가 n보다 크면 중단
    if current_num > n:
        return

    # 현재 숫자가 n보다 작거나 같으면 최댓값 갱신
    max_result = max(max_result, current_num)

    # 다음 자릿수 탐색
    for digit in data:
        # 현재 숫자에 새 자릿수 추가
        next_num = current_num * 10 + digit

        # 다음 숫자가 n보다 이미 크면 더 탐색할 필요 없음
        if next_num > n:
            continue

        recursion(next_num)


for first_digit in data:
    recursion(first_digit)

print(max_result)
