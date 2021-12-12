import hashlib

val = 'yzbqklnj'
i = 0
hashed = '      '

while hashed[:6] != '000000':
    i += 1
    hashed = hashlib.md5(f'{val}{i}'.encode('utf-8')).hexdigest()

print(i)
