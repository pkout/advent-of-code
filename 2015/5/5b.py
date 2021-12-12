def has_2_pairs_without_overlap(string):
    for i in range(len(string) - 3):
        pair = string[i:i+2]

        if pair in string[i+2:]:
            return True

    return False



def has_1_letter_repeat_1_between(string):
    for i in range(len(string)-3):
        if string[i] == string[i+2]:
            return True

    return False


nice = []

with open('data.txt', 'r') as f:
    for string in [s.strip() for s in f.readlines()]:
        if has_2_pairs_without_overlap(string) and has_1_letter_repeat_1_between(string):
            nice.append(string)


print(len(nice))
