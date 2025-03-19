
input_list = []

for _ in range(3):
    input_list.append(input())

def check_fizzbuzz(data):
    if data % 3 == 0 and data % 5 == 0:
        print("FizzBuzz")
    elif data % 3 == 0 and data % 5 != 0:
        print("Fizz")
    elif data % 3 != 0 and data % 5 == 0:
        print("Buzz")
    else:
        print(data)

memory_num = 0

for i in input_list:
    if i.isdigit():
        memory_num = int(i)
    else:
        memory_num += 1

check_fizzbuzz(memory_num + 1)