with open('data.txt', 'r') as f:
    total_length = 0

    for line in f.readlines():
        dims = sorted([int(n) for n in line.strip().split('x')])
        perimeter = dims[0]*2 + dims[1]*2
        slack = dims[0] * dims[1] * dims[2]
        length = perimeter + slack
        total_length += length

print(total_length)
