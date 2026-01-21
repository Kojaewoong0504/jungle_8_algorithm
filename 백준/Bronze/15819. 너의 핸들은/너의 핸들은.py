N,I = map(int, input().split())
 
arr = []
 
for _ in range(N):
    handle = input()
    arr.append(handle)
 
arr.sort()
 
print(arr[I-1])
