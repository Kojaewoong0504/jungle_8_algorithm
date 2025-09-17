from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    curr = 0
    waiting = deque(truck_weights)
    
    while waiting or curr > 0:
        time += 1
        curr -= bridge.popleft()
        
        if waiting and curr + waiting[0] <= weight:
            w = waiting.popleft()
            bridge.append(w)
            curr += w
        else:
            bridge.append(0)
    
    return time