def sort(s):
    for i in range(1, len(s)):
        j = i
        while j > 0 and s[j] > s[j-1]:
            s[j-1], s[j] = s[j], s[j-1]
            j -= 1

    return s


print(sort([]))
print(sort([3]))
print(sort([3, 4, 4, 5]))
print(sort([3, 4, 2, 5]))
print(sort([4, 3, 2, 1]))
print(sort([1, 2, 3, 4]))
