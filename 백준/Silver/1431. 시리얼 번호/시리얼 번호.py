n = int(input())
data = list(input().strip() for _ in range(n))

def digit_sum(s):
    return sum(int(ch) for ch in s if ch.isdigit())

data.sort(key= lambda x : (len(x), digit_sum(x), x))

print("\n".join(data))