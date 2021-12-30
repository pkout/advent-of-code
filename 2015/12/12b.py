import json

with open('data.txt', 'r') as f:
    data = f.read().strip()

total = 0

def traverse(d):
    global total

    if isinstance(d, int):
        total += d

    elif isinstance(d, dict):
        if has_red(d.values()):
            return

        for v in d.values():
            traverse(v)

    elif isinstance(d, list):
        for it in d:
            traverse(it)

def has_red(values):
    for v in values:
        if v == 'red':
            return True

    return False

data_dict = json.loads(data)
traverse(data_dict)

print(f'Sum: {total}')
