from my_modules import gen_random_index_list
from my_modules import shuffle_pass
from my_modules import get_pwd_len
from my_modules import get_char_types
from my_modules import calc_sect_len
from my_modules import pass_generator


def convert_char_types(choices: list) -> list:
    "Function converts y/n to True/False list"
    converted_list = []
    for choice in choices:
        if choice == 'y':
            converted_list.append(True)
        else:
            converted_list.append(False)
    return converted_list


def main():
    new_std_input = []
    pass_len = get_pwd_len()
    new_std_input.append(pass_len)
    raw_char_types = get_char_types()
    char_types = convert_char_types(raw_char_types)
    for chr_type in char_types:
        new_std_input.append(chr_type)
    cld = calc_sect_len(new_std_input)

    print("Debug:", new_std_input)
    raw_pass = pass_generator(new_std_input, cld)
    print(shuffle_pass(raw_pass))


if __name__ == '__main__':
    main()
