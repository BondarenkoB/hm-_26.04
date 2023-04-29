with open('test.txt', 'r') as file:
    contents = file.readlines()

contents.pop(2) 

with open('test.txt', 'w') as file:
    contents = ''.join(contents)
    file.write(contents)

