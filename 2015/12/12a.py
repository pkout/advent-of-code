import re

with open('data.txt', 'r') as f:
    data = f.read().strip()

total = sum([int(s) for s in re.findall('-?\d+', data)])

print(f'Sum: {total}')
