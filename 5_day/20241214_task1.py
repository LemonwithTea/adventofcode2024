file = open('input_default.txt', 'r')
default_list = []

for line in file:
    default_list.append(line.strip('\n'))

a = default_list.index('')
rule_list = default_list[:a]
initial_list = default_list[a+1:]

default_list.clear()

for i in range(len(initial_list)):

    len_j = len(initial_list[i])
    for j in range(len_j):
        for k in range(len_j - j):
            for m in range(len(rule_list)):
                if rule_list[m] == initial_list[k]:
                    iter_rule_list = rule_list[m]
                else:
                    iter_rule_list = None
                    continue
        initial_list[k]
        print(initial_list[i][j])