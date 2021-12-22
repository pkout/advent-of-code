def perm(l):
    if len(l) == 1:
        return [l]
    
    perms = []

    for i in range(len(l)):
        hold = l[i]
        remainder = l[:i] + l[i+1:]

        for p in perm(remainder):
            perms.append([hold] + p)

    return perms

print(perm([1, 2, 3, 4]))
print(len(perm([1, 2, 3, 4])))
