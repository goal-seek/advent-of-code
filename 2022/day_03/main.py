"""
--- Part One ---
"""

file_name = "input.txt"

input_list = []
with open(file_name) as file:
    for line in file:
        string = line.rstrip('\n')
        input_list.append([string[:len(string)//2], string[len(string)//2:]])

#print(input_list)

error_items = []
for i in input_list:
    set_1 = set(i[0])
    set_2 = set(i[1])
    error_items.append(''.join(set_1.intersection(set_2)))

#print(error_items)

def get_priorities(items):
    priorities = []
    for i in items:
        if i.isupper():
            val = ord(i)-38
        elif i.islower():
            val = ord(i)-96
        priorities.append(val)
    return priorities

#print(priorities)
priorities = get_priorities(error_items)
total_value = sum(priorities)
print(total_value)

"""
--- Part Two ---
"""
i = 0
input_list = []
group = []
with open(file_name) as file:
    for line in file:
        i = i + 1
        string = line.rstrip('\n')
        group.append(string)
        if i == 3:
            input_list.append(group)
            group = []
            i = 0

badges = []
for group in input_list:
    set_1 = set(group[0])
    set_2 = set(group[1])
    set_3 = set(group[2])
    badges.append(''.join(set_1.intersection(set_2.intersection(set_3))))

print(badges)

priorities = get_priorities(badges)
total_value = sum(priorities)
print(total_value)
