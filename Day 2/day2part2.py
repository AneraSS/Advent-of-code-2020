# How many passwords are valid according to their policies?
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.


def get_limits(string):
    splitted1 = string.split(':')
    splitted2 = splitted1[0].split(' ')
    splitted3 = splitted2[0].split('-')
    minimum = int(splitted3[0])
    maximum = int(splitted3[1])
    return minimum, maximum


def get_letter(string):
    letter = ""
    for character in string:
        if character.isalpha():
            letter = character
            break
    return letter


def get_password(string):
    return string.split(':')[1].strip()


def is_valid(string):
    letter = get_letter(string)
    minimum, maximum = get_limits(string)
    password = get_password(string)
    if (letter == password[minimum-1]) ^ (letter == password[maximum-1]): # ^ means XOR - exclusive or, either
        return True
    else:
        return False

with open('input.txt') as f:
    count_valid = 0
    for line in f:
        if is_valid(line):
            count_valid += 1
    print(count_valid)

# solution obtained - 737