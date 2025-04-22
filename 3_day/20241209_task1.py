import re

def mul(num_1, num_2):
    return int(num_1) * int(num_2)

f = open('input.txt', 'r')
source_string = f.read()
f.close()
target_list = re.findall("mul\(\d{1,},\d{1,}\)", source_string)

sum_num = 0

for i in range(len(target_list)):
    sum_num = sum_num + eval(target_list[i])
print(sum_num)