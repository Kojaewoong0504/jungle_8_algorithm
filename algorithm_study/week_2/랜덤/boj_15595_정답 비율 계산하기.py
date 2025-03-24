n = int(input())
users = {}  # 사용자별 제출 기록을 저장할 딕셔너리

for _ in range(n):
    submission = input().split()
    user_id = submission[1]
    result = int(submission[2])

    # 관리자(megalusion)는 제외
    if user_id == "megalusion":
        continue

    # 사용자가 딕셔너리에 없으면 추가
    if user_id not in users:
        users[user_id] = {"correct": 0, "wrong": 0, "solved": False}

    # 이미 문제를 맞은 사용자는 더 이상 카운트하지 않음
    if users[user_id]["solved"]:
        continue

    # 제출 결과에 따라 카운트
    if result == 4:  # "맞았습니다!!"
        users[user_id]["correct"] = 1
        users[user_id]["solved"] = True
    else:  # 틀린 경우
        users[user_id]["wrong"] += 1

# 정답 비율 계산
correct_count = sum(user["correct"] for user in users.values())
wrong_count = sum(user["wrong"] for user in users.values() if user["solved"])

if correct_count == 0:
    answer_rate = 0
else:
    answer_rate = (correct_count / (correct_count + wrong_count)) * 100

print(answer_rate)
