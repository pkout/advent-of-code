import re

wires = {}

with open('data.txt', 'r') as f:
    for line in f.readlines():
        if m := re.search(r'^(\w+) -> (\w+)\n', line):
            wires[m.group(2)] = {
                'operation': 'ASSIGN', 'input1': m.group(1), 'input2': None
            }

        if m := re.search(r'^(\w+) AND (\w+) -> (\w+)\n', line):
            wires[m.group(3)] = {
                'operation': 'AND', 'input1': m.group(1), 'input2': m.group(2)
            }

        if m := re.search(r'^(\w+) OR (\w+) -> (\w+)\n', line):
            wires[m.group(3)] = {
                'operation': 'OR', 'input1': m.group(1), 'input2': m.group(2)
            }

        if m := re.search(r'^(\w+) LSHIFT (\w+) -> (\w+)\n', line):
            wires[m.group(3)] = {
                'operation': 'LSHIFT', 'input1': m.group(1), 'input2': m.group(2)
            }

        if m := re.search(r'^(\w+) RSHIFT (\w+) -> (\w+)\n', line):
            wires[m.group(3)] = {
                'operation': 'RSHIFT', 'input1': m.group(1), 'input2': m.group(2)
            }

        if m := re.search(r'^NOT (\w+) -> (\w+)\n', line):
            wires[m.group(2)] = {
                'operation': 'NOT', 'input1': m.group(1), 'input2': None
            }

def is_num(val):
    try:
        _ = int(val)
        return True
    except:
        return False

def signal_into(wire_name):
    if wire_name is None:
        return None

    if is_num(wire_name):
        return int(wire_name)

    wire = wires[wire_name]

    if is_num(wires[wire_name]):
        return wires[wire_name]

    wires[wire_name] = gate(
        wire['operation'],
        signal_into(wire['input1']),
        signal_into(wire['input2'])
    )

    return wires[wire_name]

def gate(operation, input1, input2):
    if operation == 'NOT':
        return ~input1

    if operation == 'AND':
        return input1 & input2

    if operation == 'OR':
        return input1 | input2

    if operation == 'LSHIFT':
        return input1 << input2

    if operation == 'RSHIFT':
        return input1 >> input2

    if operation == 'ASSIGN':
        return input1


wires['b'] = 956

print(signal_into('a'))
