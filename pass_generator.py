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
    include_letter_up = str(input("Do you want include upper case letters (y/n)?:"))
    include_letter_low = str(input("Do you want include lower case letters (y/n)?:"))
    include_nums = str(input("Do you want include numbers (y/n)?:"))
    include_specials = str(
        input("Do you want include special characters (y/n)?:"))

    req_list.append(pwd_len)
    if include_letter_up == 'y':
        req_list.append(True)
    else:
        req_list.append(False)

    if include_letter_low == 'y':
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
    #            pass_len , up, low, nums, special                    
    return req_list  # [8, True, True, True, True]


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
               let_idx_list = gen_random_index_list(diff - 1, len(letters))
               for index in let_idx_list:
                   final_pass.append(letters[index])
        
        if requirements[0] - sect_count < 0:
            print("Error: password lengh < requirements selected") 
            
    

    # print("section len:", sect_len)  # for debugging
    if enabled_numbers:
        num_idx_list = gen_random_index_list(sect_len + 1, len(numbers))
        for index in num_idx_list:
            final_pass.append(numbers[index])

    if enabled_letters_up:
        let_idx_list = gen_random_index_list(sect_len + 1, len(letters))
        for index in let_idx_list:
            final_pass.append(letters[index])

    if enabled_letters_low:
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
    std_reqs = collect_reqs()
    print(std_reqs)
    print(gen_pass(std_reqs))


if __name__ == '__main__':
    main()
