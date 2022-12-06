# Find the three entries that sum to 2020; what do you get if you multiply them together?
with open ('input.txt') as file_object:
    full_list = []
    for line in file_object:
        line = int(line.strip('\n'))
        full_list.append(line)

    result = 0
    for number1 in full_list:
        for number2 in full_list:
            for number3 in full_list:
                if number1+number2+number3==2020:
                    result = number1*number2*number3

    print(result)

# result obtained