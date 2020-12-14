from __future__ import print_function

count_with_2_chars = 0
count_with_3_chars = 0

def count_repeating_chars(s):
    global count_with_2_chars, count_with_3_chars
    chars = {}
    for c in s:
        chars[c] = 0
    for c in s:
        chars[c] += 1
    for c in chars:
        if chars[c] == 2:
            count_with_2_chars += 1
            break
    for c in chars:
        if chars[c] == 3:
            count_with_3_chars += 1
            break
    print(s, c, chars, count_with_2_chars, count_with_3_chars)

with open('data.txt', 'r') as f:
    codes = [ x.strip() for x in f.readlines() ]
    for code in codes:
        count_repeating_chars(code)
print(count_with_2_chars * count_with_3_chars)
