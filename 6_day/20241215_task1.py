file = open('input_default.txt', 'r')
source_list = []
for line in file:
    source_list.append(list(line.strip('\n')))
file.close()
index_x = 0
index_y = 0
for i in range(len(source_list)):
    try: 
        index_y = source_list[i].index('^')
        index_x = i
        break
    except ValueError: 
        pass
print(index_x, index_y)

tgt_sum = 0
len_x = len(source_list)
len_y = len(source_list[0])
i = index_x
j = index_y
while i <= len_x and j <= len_y:
    flag = True
    while flag == True:
        if source_list[i][j] <> '#':
            j -= 1
        else:
            i += 
