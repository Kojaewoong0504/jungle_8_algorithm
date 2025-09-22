n = int(input())
students = list(map(int, input().split()))

team_count = 0

students.sort()

st = 0
while st < n:
    cap = students[st]
    remain = n - st
    take = cap if cap <= remain else remain
    team_count += 1
    st += take

print(team_count)