arr = [5,8,4,2,6,1,3,9,7]
from typing import MutableSequence

def qsort(a: MutableSequence, left, right):
    pl = left
    pr = right
    pivot = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while a[pr] > pivot:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)


qsort(arr,0, len(arr)-1)
print(arr)


arr2 = [5,8,4,2,6,1,3,9,7]

def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    left = []
    right = []

    for element in a[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr2))