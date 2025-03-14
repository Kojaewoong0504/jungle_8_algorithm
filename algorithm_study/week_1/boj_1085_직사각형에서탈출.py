x, y, w, h = map(int,input().split())


# 1번 풀이

nx = x if w-x > x else w-x
ny = y if h-y > y else h-y

print(nx if nx < ny else ny)

# 2번 풀이 = 압축 혹은 python 함수 활용

print(min(x, y, w-x, h-y))
