with open('test.txt', 'r') as file:
    lines = file.readlines()

lines.sort()

with open('test.txt', 'w') as file:
    for line in lines:
        file.write(line)

