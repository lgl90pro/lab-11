'''Дан текстовий файл f. Отримати в файлі g кількість букв, що знаходяться в файлі
f.
Виконав: Лещенко В. О.'''

with open('f.txt', 'r') as f:
    f_read = f.read()
    count = 0
    for i in f_read:
        if i.isalpha(): # перевіряємо чи елемент буква і додаємо до лічильника
            count += 1

with open('g.txt', 'w') as g:
    g.write(str(count)) # записуємо в g кількість букв із файлу f