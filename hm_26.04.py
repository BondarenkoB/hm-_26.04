with open('test.txt', 'r') as file:
    for line in file:
        if 'Вода' in line: # в '1' можна пiдставити iнше слово
            print(line)

