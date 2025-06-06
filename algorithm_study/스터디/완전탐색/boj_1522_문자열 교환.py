s_input = input()

length_s = len(s_input)
a_num = s_input.count("a")
s_input += s_input

max_a = 0
for i in range(length_s):
    count_a = s_input[i:i+a_num].count("a")
    max_a = max(max_a, count_a)

print(a_num-max_a)