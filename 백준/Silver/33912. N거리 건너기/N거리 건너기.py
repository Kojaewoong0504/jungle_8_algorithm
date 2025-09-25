import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

pos = [0]*(N+1)
for k, x in enumerate(A):
    pos[x] = k  # 0..N-1

def time_to_reach(edges):
    T = 0
    for x in edges:
        T += (pos[x] - (T % N)) % N
    return T

cw_time  = time_to_reach(range(1, M))
ccw_time = time_to_reach(range(N, M-1, -1))

print("CW" if cw_time < ccw_time else "CCW" if ccw_time < cw_time else "EQ")
