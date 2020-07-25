from my_modules import gen_random_index_list
from my_modules import shuffle_pass
from my_modules import collect_pwd_reqs
from my_modules import get_pwd_len

spec_chars = ['!', '"', '£', '$', '%', '&', '*', '(', ')', '_', '+']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def gen_pass(requirements: list) -> str:
    sect_count = 0

    final_pass = []
    enabled_letters_up = requirements[1]
    enabled_letters_low = requirements[2]
    enabled_numbers = requirements[3]
    enabled_spec_chars = requirements[4]

    if enabled_letters_up:
        sect_count += 1
    if enabled_letters_low:
        sect_count += 1
    if enabled_numbers:
        sect_count += 1
    if enabled_spec_chars:
        sect_count += 1

    if requirements[0] % sect_count == 0:
        sect_len = int(requirements[0] / sect_count)
        print(sect_len)
    else:
        if requirements[0] - sect_count > 0:
            sect_len = int(requirements[0] / sect_count)
            diff = requirements[0] % sect_count

            if diff > 0:
                let_idx_list = gen_random_index_list(diff, len(letters))
                for index in let_idx_list:
                    final_pass.append(letters[index])

        if requirements[0] - sect_count < 0:
            print("Error: password lengh < requirements selected")

    # print("section len:", sect_len)  # for debugging
    if enabled_numbers:
        num_idx_list = gen_random_index_list(sect_len, len(numbers))
        for index in num_idx_list:
            final_pass.append(numbers[index])

    if enabled_letters_up:
        let_idx_list = gen_random_index_list(sect_len, len(letters))
        for index in let_idx_list:
            final_pass.append(letters[index])

    if enabled_letters_low:
        let_idx_list = gen_random_index_list(sect_len, len(letters))
        for index in let_idx_list:
            low_str = letters[index]
            low = low_str.lower()
            final_pass.append(low)

    if enabled_spec_chars:
        spec_idx_list = gen_random_index_list(sect_len, len(spec_chars))
        for index in spec_idx_list:
            final_pass.append(spec_chars[index])
    return final_pass


def main():
    new_std_input = []
    pass_len = get_pwd_len()
    new_std_input.append(pass_len)

    std_reqs = collect_pwd_reqs()
    print("Debug info:", std_reqs)
    print("Debug info:", gen_pass(std_reqs))
    raw_pass = gen_pass(std_reqs)
    print(shuffle_pass(raw_pass))


if __name__ == '__main__':
    main()
