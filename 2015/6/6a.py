import re

lights = {}

for x in range(1000):
    for y in range(1000):
        lights[(x, y)] = False

with open('data.txt', 'r') as f:
    for line in f.readlines():
        instr = re.findall(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        action = instr[0][0]
        x0, y0 = int(instr[0][1]), int(instr[0][2])
        x1, y1 = int(instr[0][3]), int(instr[0][4])
        print('Action:', action, x0, y0, x1, y1)

        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                if action == 'turn on':
                    lights[(x, y)] = True
                if action == 'turn off':
                    lights[(x, y)] = False
                if action == 'toggle':
                    lights[(x, y)] = not lights[(x, y)]

num_of_on_lights = 0
for x in range(1000):
    for y in range(1000):
        if lights[(x, y)]:
            num_of_on_lights += 1

print('The number of lights turned on is', num_of_on_lights)
