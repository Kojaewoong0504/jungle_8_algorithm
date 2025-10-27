import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
queue = deque()

A = []  
B = []  
C = []  

for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        student_id = command[1]  
        fav_menu = command[2]   
        queue.append((student_id, fav_menu)) 

    elif command[0] == 2:
        meal = command[1]  
        if queue:
            student_id, fav_menu = queue.popleft()  
            if fav_menu == meal:
                A.append(student_id)  
            else:
                B.append(student_id)  

while queue:
    student_id, _ = queue.popleft()
    C.append(student_id)

def print_list(lst):
    if lst:
        print(" ".join(map(str, sorted(lst))))
    else:
        print("None")

print_list(A)
print_list(B)
print_list(C)