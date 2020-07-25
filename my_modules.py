import random


def gen_random_index_list(count: int, range_len: int) -> list:
    "Function to generate list  of random numbers"
    index_list = []
    for i in range(count):
        x = random.randrange(1, range_len)
        index_list.append(x)
    return index_list


def shuffle_pass(str_list: list) -> str:
    "Function takes row character list and return shuffled character string"
    # changes str_list to different characters and shuffles
    random.shuffle(str_list)
    pass_char_list = ""
    for pass_char in str_list:
        pass_char_list += str(pass_char)
    return pass_char_list


def collect_pwd_reqs() -> list:
    "Function collects password requiremnts from STDIN"
    "Function verifies that correct/valid values are entered"
    valid_coices = ['Y', 'N', 'y', 'n']
    min_len = 4
    max_len = 30
    req_list = []
    len_valid = True
    format_valid = True

    while format_valid:
        try:
            pwd_len = int(input("Choose password lenght(characters): "))
            format_valid = False
        except ValueError:
            print("Password lenght should be digit")

    while len_valid:
        if pwd_len > min_len and pwd_len < max_len:
            req_list.append(pwd_len)
            len_valid = False
        if pwd_len < min_len:
            print("Minimum password lenght is 4, try again")
            pwd_len = int(input("Choose password lenght(characters): "))

        if pwd_len > max_len:
            print("Max password lenght is 30 characters, try again")
            pwd_len = int(input("Choose password lenght(characters): "))

    include_letter_up = str(
        input("Do you want include upper case letters (y/n)?:"))
    include_letter_low = str(
        input("Do you want include lower case letters (y/n)?:"))
    include_nums = str(input("Do you want include numbers (y/n)?:"))
    include_specials = str(
        input("Do you want include special characters (y/n)?:"))

    req_list.append(include_letter_up)
    req_list.append(include_letter_low)
    req_list.append(include_nums)
    req_list.append(include_specials)

    return req_list


def get_pwd_len() -> int:
    "Function collects password requiremnts from STDIN and "
    "validates that value is int and > 4 and < 30"
    "Return int:  pwd_len"
    min_len = 4
    max_len = 30
    len_valid = True
    format_valid = True

    while format_valid:
        try:
            pwd_len = int(input("Choose password lenght(characters): "))
            format_valid = False
        except ValueError:
            print("Password lenght should be digit")

    while len_valid:
        if pwd_len > min_len and pwd_len < max_len:
            return pwd_len
        if pwd_len < min_len:
            print("Minimum password lenght is 4, try again")
            pwd_len = int(input("Choose password lenght(characters): "))

        if pwd_len > max_len:
            print("Max password lenght is 30 characters, try again")
            pwd_len = int(input("Choose password lenght(characters): "))


def get_char_types() -> list:
    "Function collects input from STDIN"
    "No error checking for invalid inputs TODO fix that"
    req_list = []
    include_letter_up = str(
        input("Do you want include upper case letters (y/n)?:"))
    include_letter_low = str(
        input("Do you want include lower case letters (y/n)?:"))
    include_nums = str(input("Do you want include numbers (y/n)?:"))
    include_specials = str(
        input("Do you want include special characters (y/n)?:"))

    req_list.append(include_letter_up)
    req_list.append(include_letter_low)
    req_list.append(include_nums)
    req_list.append(include_specials)
    return req_list


def calc_sect_len(req_list: list, pass_len: int) -> int:
    "Function calculates section lenght for each character type"
    sect_len = 0
    for req in req_list:
        if req is True:
            sect_len += 1
    return pass_len // sect_len
