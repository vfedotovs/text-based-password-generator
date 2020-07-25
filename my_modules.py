import random


spec_chars = ['!', '"', '£', '$', '%', '&', '*', '(', ')', '_', '+']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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


def calc_sect_len(req_list: list) -> list:
    "Function calculates section lenght for each character type"
    sect_count = 0
    count_len_diff = []
    pass_len = req_list[0]

    for req in req_list:
        if req is True:
            sect_count += 1

    sect_len = pass_len // sect_count
    diff = pass_len - (sect_count * sect_len)

    count_len_diff.append(sect_count)
    count_len_diff.append(sect_len)
    count_len_diff.append(diff)

    return count_len_diff


def pass_generator(requirements: list, count_len_diff: list) -> str:
    # sect_count = count_len_diff[0]
    sect_len = count_len_diff[1]
    diff = count_len_diff[2]
    final_pass = []

    if diff > 0:
        let_idx_list = gen_random_index_list(diff, len(letters))
        for index in let_idx_list:
            final_pass.append(letters[index])

    if requirements[3]:
        num_idx_list = gen_random_index_list(sect_len, len(numbers))
        for index in num_idx_list:
            final_pass.append(numbers[index])

    # enabled_letters_up
    if requirements[1]:
        let_idx_list = gen_random_index_list(sect_len, len(letters))
        for index in let_idx_list:
            final_pass.append(letters[index])

    # enabled_letters_low
    if requirements[2]:
        let_idx_list = gen_random_index_list(sect_len, len(letters))
        for index in let_idx_list:
            low_str = letters[index]
            low = low_str.lower()
            final_pass.append(low)

    if requirements[4]:
        spec_idx_list = gen_random_index_list(sect_len, len(spec_chars))
        for index in spec_idx_list:
            final_pass.append(spec_chars[index])

    return final_pass
