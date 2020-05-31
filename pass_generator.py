import random


spec_chars = ['!', '"', '£', '$', '%', '&', '*', '(', ')', '_', '+']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def gen_random_index_list(count: int, range_len: int) -> list:
    index_list = []
    for i in range(1, count):
        x = random.randrange(1, range_len)
        index_list.append(x)
    return index_list


def collect_reqs() -> list:
    req_list = []
    pwd_len = int(input("Please chose password lenght:"))
    include_letter = str(input("Do you want include letters (y/n)?:"))
    include_nums = str(input("Do you want include numbers (y/n)?:"))
    include_specials = str(
        input("Do you want include special characters (y/n)?:"))

    req_list.append(pwd_len)
    if include_letter == 'y':
        req_list.append(True)
    else:
        req_list.append(False)

    if include_nums == 'y':
        req_list.append(True)
    else:
        req_list.append(False)

    if include_specials == 'y':
        req_list.append(True)
    else:
        req_list.append(False)
    return req_list


def calculate_section_len(reqs: list) -> int:
    """ if letters x2 nums x 1 and specials x 1"""
    tot_len = reqs[0]
    sum = 0
    if reqs[1]:
        sum += 2  # for upper and lower case
    if reqs[2]:
        sum += 1
    if reqs[3]:
        sum += 1
    return tot_len // sum


def gen_pass(sect_len: int,
             enabled_letters: bool,
             enabled_numbers: bool,
             enabled_spec_chars: bool) -> str:
    # print("section len:", sect_len)  # for debugging
    final_pass = []
    if enabled_numbers:
        num_idx_list = gen_random_index_list(sect_len + 1, len(numbers))
        for index in num_idx_list:
            final_pass.append(numbers[index])

    if enabled_letters:
        let_idx_list = gen_random_index_list(sect_len + 1, len(letters))
        for index in let_idx_list:
            final_pass.append(letters[index])

    if enabled_letters:
        let_idx_list = gen_random_index_list(sect_len + 1, len(letters))
        for index in let_idx_list:
            low_str = letters[index]
            low = low_str.lower()
            final_pass.append(low)

    if enabled_spec_chars:
        spec_idx_list = gen_random_index_list(sect_len + 1, len(spec_chars))
        for index in spec_idx_list:
            final_pass.append(spec_chars[index])

    random.shuffle(final_pass)

    s = ""
    for j in final_pass:
        s += str(j)
    return s


def main():
    rlist = collect_reqs()
    slen = calculate_section_len(rlist)
    print(gen_pass(slen, rlist[1], rlist[2], rlist[3]))


if __name__ == '__main__':
    main()
