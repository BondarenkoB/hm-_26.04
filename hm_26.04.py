with open('test.txt', 'r') as file:
    lines = set()
    duplicates = set()
    
    for line in file:
        if line in lines:
            duplicates.add(line)
        else:
            lines.add(line)

if duplicates:
    print(f'Файл має дублікати рядків: {duplicates}')
else:
    print('Файл не має дублікати рядків')

