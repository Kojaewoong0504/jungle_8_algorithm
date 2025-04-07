n = int(input())
rope = list()

for i in range(n):
    rope.append(int(input()))

rope.sort()

max_weight = -1
len_rope = len(rope)
idx = 0

while(True):
    if len_rope <= 0:
         break
    if rope[idx] * len_rope > max_weight:
        max_weight = rope[idx] * len_rope
    idx += 1
    len_rope -= 1

print(max_weight)