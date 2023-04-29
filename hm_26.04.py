with open('test.txt', 'r') as file:
    contents = file.read()
    word_count = len(contents.split())
    print(f'Кількість слів: {word_count}')

