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
    "Function verifys that correct/valid values are entered"
    pass


def calc_sect_len(req_kist: list) -> int:
    "Function calculates section lenght for each character type"
    pass
