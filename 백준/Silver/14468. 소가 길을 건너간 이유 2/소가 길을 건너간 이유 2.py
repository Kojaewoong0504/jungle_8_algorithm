import sys
input = sys.stdin.readline
s = input().strip()
result = 0 
for start in range(52):
    for end in range(start+1,52): 
        if s[start] == s[end]: 
            cows = s[start:end+1]
            for i in cows:
                if cows.count(i) == 1:
                    result += 1
            break
print(result // 2)