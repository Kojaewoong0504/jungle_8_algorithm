
string = input().split(' ')
month = string[0]
dd = int(string[1][:-1])
yyyy = int(string[2])
hh, mm = map(int, string[3].split(':'))

month_name = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]


month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0):
    month_day[1] += 1

all_time = sum(month_day) * 24 * 60
month_idx = month_name.index(month)
current_time = (sum(month_day[:month_idx]) + dd - 1) * 24 * 60 + hh * 60 + mm
print(current_time / all_time * 100)