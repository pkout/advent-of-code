visited_coords = [(0, 0)]

coords = {
    's': [0, 0],
    'r': [0, 0]
}

turn = 'santa'

with open('data.txt', 'r') as f:
    for direction in f.read():
        if turn == 'santa':
            mover = coords['s']
        else:
            mover = coords['r']

        if direction == '^':
            mover[1] += 1
        if direction == '>':
            mover[0] += 1
        if direction == 'v':
            mover[1] -= 1
        if direction == '<':
            mover[0] -= 1

        visited_coords.append(tuple(mover))

        if turn == 'santa':
            turn = 'robot'
        else:
            turn = 'santa'

visited_coords = set(visited_coords)
print(len(visited_coords))
