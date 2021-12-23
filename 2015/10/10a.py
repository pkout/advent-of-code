data = '1321131112'

def look_and_say(data):
    num = data[0]
    count = 1
    output = ''

    for i in range(1, len(data)):
        if data[i] == num:
            count +=1
        else:
            output += f'{count}{num}'
            count = 1
            num = data[i]

        if i == len(data) - 1:
            output += f'{count}{num}'

    return output

for i in range(40):
    data = look_and_say(data)

print(len(data))
