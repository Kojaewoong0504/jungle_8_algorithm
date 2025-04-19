from collections import Counter

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
cnt = 0


def sort_matrix(list_line):
    num_count = Counter(x for x in list_line if x != 0)  # 0 무시
    sorted_num = sorted(num_count.items(), key=lambda x: (x[1], x[0]))
    result = []
    for num, freq in sorted_num:
        result.extend([num, freq])
    return result[:100]  # 길이 100 제한

# 최대 100 까지 진행한다. 100이 될 때 까지 찾지 못하면 -1 출력

for i in range(101):
    if r - 1 < len(matrix) and c - 1 < len(matrix[0]) and matrix[r - 1][c - 1] == k:
        print(i)
        exit(0)
    if len(matrix) >= len(matrix[0]):  # R 연산
        new_matrix = []
        max_len = 0
        for row in matrix:
            new_row = sort_matrix(row)
            max_len = max(max_len, len(new_row))
            new_matrix.append(new_row)
        for row in new_matrix:
            row += [0] * (max_len - len(row))  # 0 padding
        matrix = new_matrix

    else:  # C 연산
        transposed = list(zip(*matrix))  # 열을 행처럼
        new_cols = []
        max_len = 0
        for col in transposed:
            new_col = sort_matrix(col)
            max_len = max(max_len, len(new_col))
            new_cols.append(new_col)
        for col in new_cols:
            col += [0] * (max_len - len(col))  # 0 padding
        # 다시 전치해서 원래 행 기준으로
        matrix = [list(row) for row in zip(*new_cols)]
print(-1)  # 100초 동안 못 찾은 경우
