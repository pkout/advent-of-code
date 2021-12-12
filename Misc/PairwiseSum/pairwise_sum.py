# 1+2, 2+3, 3+4, 4+5
# 3 5 7 9 => 24

def pws(n):
    total = 0

    # start from 1
    for i in range(1, n):
        total += 2 * i + 1

    return total

print(pws(5))
