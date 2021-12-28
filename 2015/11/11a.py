init_password = 'hepxcrrq'

def find_valid_password(password):
    password = list(password)

    i = len(password) - 1
    password_count = 0

    for p in gen_password(password, i):
        if is_valid(p):
            print(f'Password: {p}')
            password_count += 1

        if password_count == 2:
            break


def gen_password(password, i):
    while i > -1:
        if password[i] == 'z':
            i -= 1
            continue

        char_ord = ord(password[i])
        password[i] = chr(char_ord + 1)

        for j in range(i + 1, len(password)):
            password[j] = 'a'

        i = len(password) - 1

        yield ''.join(password)


def is_valid(password):
    return \
        has_3_straight_letters(password) \
        and has_illegal_letters(password) \
        and has_2_non_overlapping_pairs(password)


def has_3_straight_letters(val):
    i = 0

    while True:
        if ord(val[i]) == ord(val[i + 1]) - 1 and ord(val[i]) == ord(val[i + 2]) - 2:
            return True

        if i == len(val) - 3:
            break

        i += 1

    return False


def has_illegal_letters(val):
    return not any(list(filter(lambda n: n in val, ['i', 'o', 'l'])))


def has_2_non_overlapping_pairs(val):
    i = 0
    pairs = []

    while True:
        if val[i] == val[i + 1] and val[i] not in pairs:
            pairs.append(val[i])

        if len(pairs) == 2:
            return True

        if i == len(val) - 2:
            break

        i += 1

    return False

assert is_valid('abcffggcd')
assert not is_valid('abcffigd')
assert is_valid('aabbfghd')

find_valid_password(init_password)
