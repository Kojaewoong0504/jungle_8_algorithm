def recursion(height, start, end):
    if start > end:
        return 0
    if start == end:
        return height[start]

    mid = (start + end) // 2

    left_max = recursion(height, start, mid)
    right_max = recursion(height, mid+1, end)

    cross_max = find_center_max(height, start, mid, end)

    return max(left_max, right_max, cross_max)


def find_center_max(height, start, mid, end):
    left = mid
    right = mid + 1
    current_height = min(height[left], height[right])
    max_area = current_height * 2

    current_width = 2
    while left > start or right < end:
        if left == start:
            right += 1
            current_height = min(current_height, height[right])
        elif right == end:
            left -= 1
            current_height = min(current_height, height[left])
        elif height[left - 1] > height[right + 1]:
            left -= 1
            current_height = min(current_height, height[left])
        else:
            right += 1
            current_height = min(current_height, height[right])
        current_width += 1
        max_area = max(max_area, current_height * current_width)
    return max_area


n = int(input())
input_data = [int(input()) for _ in range(n)]

print(recursion(input_data, 0, n-1))
