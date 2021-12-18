import re

code_chars_total = 0
memory_chars_total = 0

with open('data.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        count_extra_chars_slash = 0
        count_extra_chars_double_quote = 0
        count_extra_chars_hex = 0
        code_chars_total += len(line)
        in_memory_line = line.strip()[1:-1]

        if m := re.findall(r'\\\\', in_memory_line):
            count_extra_chars_slash = len(m)

        if m := re.findall(r'\\\"', in_memory_line):
            count_extra_chars_double_quote = len(m)

        if m := re.findall(r'\\x[a-f0-9]{2}', in_memory_line):
            count_extra_chars_hex = len(m) * 3

        count_in_memory_line_chars = len(in_memory_line) - \
            count_extra_chars_slash - \
            count_extra_chars_double_quote - \
            count_extra_chars_hex

        memory_chars_total += count_in_memory_line_chars
            
print(code_chars_total - memory_chars_total)
