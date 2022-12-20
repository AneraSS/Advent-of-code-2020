# How many passwords are valid according to their policies?

def get_limits(string):
    splitted1 = string.split(':')
    splitted2 = splitted1[0].split(' ')
    splitted3 = splitted2[0].split('-')
    minimum = splitted3[0]
    maximum = splitted3[1]
    return minimum, maximum


def get_letter(string):
    letter = ""
    for character in string:
        if character.isalpha():
            letter += character
            break
    return letter

def get_password(string):
    new_string = string.split(':')
    collect_password = new_string[1]
    return collect_password

def is_valid(string):
    letter = get_letter(string)
    minimum, maximum = get_limits(string)
    password = get_password(string)
    counter = 0
    for character in password:
        if character == letter:
            counter += 1
    if (int(counter) >= int(minimum)) and (int(counter) <= int(maximum)):
        return True
    else:
        return False


with open('input.txt') as f:
    count_valid = 0
    for line in f:
        if is_valid(line):
            count_valid += 1
    print(count_valid)

# solution obtained - 645