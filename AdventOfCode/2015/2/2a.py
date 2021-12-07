with open('data.txt', 'r') as f:
    total_area = 0

    for line in f.readlines():
        dims = sorted([int(n) for n in line.strip().split('x')])
        area = dims[0]*dims[1]*2 + dims[1]*dims[2]*2 + dims[0]*dims[2]*2 + dims[0]*dims[1]
        
        total_area += area

print(total_area)
