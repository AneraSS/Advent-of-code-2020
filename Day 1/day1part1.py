# Find the two entries that sum to 2020; what do you get if you multiply them together?

with open ('input.txt') as file_object:
    full_list = []
    for line in file_object:
        line = int(line.strip('\n'))
        full_list.append(line)

    result = 0
    for current_number in full_list:
        for number in full_list:
            if current_number+number==2020:
                result = current_number*number

    print(result)

#result obtained