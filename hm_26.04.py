with open('test.txt', 'r') as file:
    if 'string' in file.read():
        print('Рядок знайдено')
    else:
        print('Рядок не знайдено')

