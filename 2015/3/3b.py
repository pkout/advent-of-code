visited_coords = [(0, 0)]
xs, ys = 0, 0
xr, yr = 0, 0

turn = 'santa'

with open('data.txt', 'r') as f:
    for direction in f.read():
        if turn == 'santa':
            if direction == '^':
                ys += 1
            if direction == '>':
                xs += 1
            if direction == 'v':
                ys -= 1
            if direction == '<':
                xs -= 1
            visited_coords.append((xs, ys))
        else:
            if direction == '^':
                yr += 1
            if direction == '>':
                xr += 1
            if direction == 'v':
                yr -= 1
            if direction == '<':
                xr -= 1
            visited_coords.append((xr, yr))

        if turn == 'santa':
            turn = 'robot'
        else:
            turn = 'santa'

visited_coords = set(visited_coords)
print(len(visited_coords))
