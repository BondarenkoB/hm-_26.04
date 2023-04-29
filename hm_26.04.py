with open('test.txt', 'r') as file:
    # Зчитуємо весь вміст файлу
    file_content = file.read()

# Замінюємо рядок
new_file_content = file_content.replace('сіль, лавровий лист, зелень – за смаком.', 'salt, bay leaf, herbs - to taste.')

with open('test.txt', 'w') as file:
    # Записуємо новий вміст у файл
    file.write(new_file_content)
