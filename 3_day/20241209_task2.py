import re

def mul(num_1, num_2):
    return int(num_1) * int(num_2)

f = open('input.txt', 'r')
source_string = f.read()
f.close()
target_list = re.findall("do\(\)|don't\(\)|mul\(\d{1,},\d{1,}\)", source_string)
print(target_list)

sum_num = 0
flag = True

for i in range(len(target_list)):
    print(flag)
    if target_list[i] == "don't()":
        flag = False
        continue
    elif target_list[i] == "do()":
        flag = True
        continue
    if flag == True:
        print(target_list[i])
        sum_num = sum_num + eval(target_list[i])
print(sum_num)