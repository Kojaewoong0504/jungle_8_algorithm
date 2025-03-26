n, w, l = map(int, input().split())
weights = list(map(int, input().split()))

bridge = [0] * w

time = 0

while bridge:
    time += 1

    bridge.pop(0)

    if weights:
        if sum(bridge) + weights[0] <= l:
            bridge.append(weights.pop(0))
        else:
            bridge.append(0)
print(time)