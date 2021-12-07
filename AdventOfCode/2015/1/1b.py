with open('data.txt', 'r') as f:
    data = f.read().strip()

floor_num = 0
position = 0

for direction in data:
    position += 1

    if direction == '(':
        floor_num += 1
    else:
        floor_num -= 1

    if floor_num == -1:
        print(position)
        break
