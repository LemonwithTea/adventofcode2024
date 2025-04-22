f = open('input_default.txt', 'r')
source_list = [x.split() for x in [line for line in f]]
f.close()

list_a = [int(x[0]) for x in source_list]
list_a.sort()

list_b = [int(x[1]) for x in source_list]
list_b.sort()

dest_sum = 0
for i in range(len(list_a)):
    dest_sum = dest_sum + abs(list_a[i] - list_b[i])
print(dest_sum)
