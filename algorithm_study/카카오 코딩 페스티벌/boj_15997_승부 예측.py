from collections import defaultdict


def game(n, p):
    if n == 6:  # 조별 리그 6경기를 모두 마쳤을 때
        nationRank = sorted(list(nationPoint.items()),
                            key=lambda x: x[1], reverse=True)  # 승점이 높은 순으로 나라 정렬

        # 4개의 나라가 승점이 같을 때
        # 4팀 중 2팀을 추첨해야 하므로, 현재 확률 p에 2/4를 곱해준다.
        if nationRank[0][1] == nationRank[1][1] == nationRank[2][1] == nationRank[3][1]:
            percentage[nationRank[0][0]] += (p / 2)
            percentage[nationRank[1][0]] += (p / 2)
            percentage[nationRank[2][0]] += (p / 2)
            percentage[nationRank[3][0]] += (p / 2)

        # 1위 == 2위 == 3위 > 4위일 때,
        # 3팀 중 2팀을 추첨해야 하므로, 현재 확률 p에 2/3을 곱해준다.
        elif nationRank[0][1] == nationRank[1][1] == nationRank[2][1] > nationRank[3][1]:
            percentage[nationRank[0][0]] += (p * (2 / 3))
            percentage[nationRank[1][0]] += (p * (2 / 3))
            percentage[nationRank[2][0]] += (p * (2 / 3))

        # 1위 > 2위 == 3위 == 4위일 때,
        # 3팀 중 1팀을 추첨해야 하므로, 현재 확률 p에 1/3을 곱해준다.
        # 1위 팀은 현재 확률 p를 더해준다.
        elif nationRank[0][1] > nationRank[1][1] == nationRank[2][1] == nationRank[3][1]:
            percentage[nationRank[0][0]] += p
            percentage[nationRank[1][0]] += (p * (1 / 3))
            percentage[nationRank[2][0]] += (p * (1 / 3))
            percentage[nationRank[3][0]] += (p * (1 / 3))

        # 1위 > 2위 == 3위 > 4위일 때,
        # 2팀 중 1팀을 추첨해야 하므로, 현재 확률 p에 1/2을 곱해준다.
        # 1위 팀은 현재 확률 p를 더해준다.
        elif nationRank[0][1] > nationRank[1][1] == nationRank[2][1] > nationRank[3][1]:
            percentage[nationRank[0][0]] += p
            percentage[nationRank[1][0]] += (p * (1 / 2))
            percentage[nationRank[2][0]] += (p * (1 / 2))

        # 나머지 1위와 2위가 확실히 정해졌을 경우
        # 두 팀에 현재 확률 p를 더해준다.
        else:
            percentage[nationRank[0][0]] += p
            percentage[nationRank[1][0]] += p

        return

    A, B, win, draw, lose = games[n][0], games[n][1], float(
        games[n][2]), float(games[n][3]), float(games[n][4])

    if win != 0.0:  # A팀이 이길 확률이 있을 때
        nationPoint[A] += 3  # A팀에 승점 3점을 더해 주고
        game(n + 1, p * win)  # A팀이 이기는 경우의 확률을 곱해주고 다음 경기로 넘어간다
        nationPoint[A] -= 3  # 다시 A팀의 승점을 원래대로 돌려준다

    if draw != 0.0:  # A와 B팀이 비길 확률이 있을 때
        nationPoint[A] += 1  # A팀과 B팀에 승점 1점을 더해 주고
        nationPoint[B] += 1
        game(n + 1, p * draw)  # 두 팀의 비길 확률을 곱해주고 다음 경기로 넘어간다
        nationPoint[A] -= 1
        nationPoint[B] -= 1

    if lose != 0.0:  # A팀이 질 확률이 있을 때
        nationPoint[B] += 3  # B팀에 승점 3점을 더해 주고
        game(n + 1, p * lose)  # A팀이 직 확률을 곱해주고 다음 경기로 넘어간다
        nationPoint[B] -= 3

nations = list(map(str, input().split()))  # 나라 리스트
games = []  # 조별 리그 경기
percentage = defaultdict(float)  # 각 나라의 다음 라운드 진출 확률
nationPoint = {}  # 조별 리그 경기를 마쳤을 때 각 나라의 승점

for _ in range(6):
    games.append(list(map(str, input().split())))

for nation in nations:
    nationPoint[nation] = 0

game(0, 1)  # game 진행

for nation in nations:
    print(percentage[nation])