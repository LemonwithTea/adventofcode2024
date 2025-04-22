f = open('input.txt', 'r')
source_list = [x.split() for x in [line for line in f]]
f.close()

list_a = [int(x[0]) for x in source_list]
list_a.sort()

list_b = [int(x[1]) for x in source_list]
list_b.sort()

dict_a = dict()
dict_b = dict()
count_a = 0
count_b = 0

for i in range(len(list_a)):
    if list_a[i] not in dict_a:
        dict_a[list_a[i]] = 1
    else:
        dict_a[list_a[i]] = dict_a[list_a[i]] + 1

    if list_b[i] not in dict_b:
        dict_b[list_b[i]] = 1
    else:
        dict_b[list_b[i]] = dict_b[list_b[i]] + 1

multy_sum = 0
for key, iter_value in dict_a.items():
    try:
        value = dict_b[key]
    except KeyError:
        value = 0
    multy_sum = multy_sum + value * key * iter_value
print(multy_sum)