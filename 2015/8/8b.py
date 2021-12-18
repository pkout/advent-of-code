import re

memory_chars_total = 0
code_chars_total = 0

with open('data.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        count_extra_chars_slash = 0
        count_extra_chars_double_quote = 0
        memory_chars_total += len(line)
        code_line = line

        for i in range(len(code_line)):
            if code_line[i] == '\\':
                count_extra_chars_slash += 1

            if code_line[i] == r'"':
                count_extra_chars_double_quote += 1

        count_code_line_chars = len(code_line) + \
            count_extra_chars_slash + \
            count_extra_chars_double_quote + \
            2 # surrounding quotes

        code_chars_total += count_code_line_chars

print(code_chars_total - memory_chars_total)
