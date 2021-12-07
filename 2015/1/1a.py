with open('data.txt', 'r') as f:
    data = f.read().strip()

floor_num = 0

for direction in data:
    if direction == '(':
        floor_num += 1
    else:
        floor_num -=1

print(floor_num)
