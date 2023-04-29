import re
with open('test.txt', 'r') as file:
    contents = file.read()
    numbers = re.findall(r'\d+', contents)
    for number in numbers:
        print(number)
