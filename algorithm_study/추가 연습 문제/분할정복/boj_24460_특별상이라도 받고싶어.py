n = int(input())
chair = [list(map(int, input().split())) for _ in range(n)]

def special(start, end, n):
    if n == 1:
        return chair[start][end]
    temp = []
    half = n//2
    temp.append(special(start, end, half))
    temp.append(special(start, end+half, half))
    temp.append(special(start+half, end, half))
    temp.append(special(start+half, end+half, half))
    return sorted(temp)[1]


print(special(0, 0, n))
