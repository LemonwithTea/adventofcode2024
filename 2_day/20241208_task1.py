f = open('input.txt', 'r')
source_list = [x.split() for x in [line for line in f]]
f.close()

save_count = 0
flag_count = False
flag_diff = False
mult = 1

for i, item in enumerate(source_list):
    
    item_len = len(item)
    F = 1
    j = 0
    plus_flg = True
    minus_flg = True

    while F == 1 and j < (item_len - 1):
        diff = int(item[j]) - int(item[j + 1])
        if (abs(diff) >= 1) and (abs(diff) <= 3):
            if diff < 0:
                minus_flg = minus_flg * True
                plus_flg = plus_flg * False
            else: 
                minus_flg = minus_flg * False
                plus_flg = plus_flg * True
            if minus_flg == plus_flg:
                F = 0
        else:
            F = 0
        j = j + 1
    if F == 1:
        save_count = save_count + 1

print(save_count)

