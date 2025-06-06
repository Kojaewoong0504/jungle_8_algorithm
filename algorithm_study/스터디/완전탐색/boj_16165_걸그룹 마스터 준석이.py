from collections import defaultdict

n, m = map(int, input().split())

idol = defaultdict(list)

for i in range(n):
    team_name = input()
    member_num = int(input())
    for j in range(member_num):
        member_name = input()
        idol[team_name].append(member_name)

for i in range(m):
    name = input()
    quiz = int(input())

    if quiz == 1:
        for j in idol:
            if name in idol[j]:
                print(j)
                continue
    else:
        team_members = idol[name]
        team_members.sort()
        for team_member in team_members:
            print(team_member)