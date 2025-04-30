
def check_heap(arr, n, parent):
    largest = parent
    left_child = (parent * 2) + 1
    right_child = (parent * 2) + 1

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        check_heap(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 + 1, -1, -1):
        check_heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        print(arr)
        arr[0], arr[i] = arr[i], arr[0]  # 루트와 끝을 교환
        check_heap(arr, i, 0)

test_list = [1,2,4,4,3,5,5,6]
heap_sort(test_list)
print(test_list)