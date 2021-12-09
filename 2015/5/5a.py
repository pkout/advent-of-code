import re

def has_forbidden(string):
    return any([x in string for x in ['ab', 'cd', 'pq', 'xy']])

def has_3_vowels(string):
    return re.match(r'(.*[aeiou].*){3,}', string) 

def has_2_consecutive_chars(string):
    return re.search(r'(.)\1{1,}', string)

nice = []

with open('data.txt', 'r') as f:
    for string in [s.strip() for s in f.readlines()]:
        if has_3_vowels(string) and has_2_consecutive_chars(string) and not has_forbidden(string):
            nice.append(string)


print(len(nice))
