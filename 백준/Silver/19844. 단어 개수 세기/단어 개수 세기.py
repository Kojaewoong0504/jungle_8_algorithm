S = list(input().replace(' ', '-').split('-'))
ans = len(S)
words = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
 
for s in S:
	# 줄인 단어로 시작하는 경우만 카운트, 이후에 모음이 올 때만
    if s[0:2] in words:
        if s[2] in ['a', 'e', 'i', 'o', 'u', 'h']:
            ans += 1
    elif s[0:3] in words:
        if s[3] in ['a', 'e', 'i', 'o', 'u', 'h']:
            ans += 1
 
print(ans)