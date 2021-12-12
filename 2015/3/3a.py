visited_coords = [(0, 0)]
x, y = 0, 0

with open('data.txt', 'r') as f:

    for direction in f.read():
        if direction == '^':
            y += 1
        if direction == '>':
            x += 1
        if direction == 'v':
            y -= 1
        if direction == '<':
            x -= 1

        visited_coords.append((x, y))

visited_coords = set(visited_coords)
print(len(visited_coords))
