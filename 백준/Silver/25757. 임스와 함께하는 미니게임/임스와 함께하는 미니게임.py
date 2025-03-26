n, type = map(str, input().split())
players = set()
n = int(n)
for _ in range(n):
    players.add(input())

if type == "Y":
    print(len(players))
elif type == "F":
    print(len(players)//2)
elif type == "O":
    print(len(players)//3)