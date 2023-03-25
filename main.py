disciplines = {
    1: 'Математика',
    2: 'Чтение',
    3: 'Прописи',
    4: 'Физкультура'
}

students = ['Иванов Вася']
marks = {}

### пример вывода значений словаря
#print("\n".join(disciplines.values()))

## Цикл ввода имён
while True:
    name = input('Введите имя ученика, 0 для отмены: ')
    if name != '0':
        students.append(name)
    else:
        break

# тестовый вывод списка учеников
# print("\n".join(students))

## Вывести пронумерованный список учеников
def print_students():
    print('\nСписок учеников класса:')
    i = 0
    for name in students:
        i+=1
        print(i, name, sep='. ')

# print("\n".join(disciplines.values()))
def print_disciplines():
    print('\nСписок уроков:')
    for i in disciplines.keys():
        print(i, disciplines[i], sep='. ')

## Цикл ввода отметок с выбором ученика
while True:
    print_students()
    student_id = int(input('0. Завершение\nВыберите ученика: '))
    if student_id != 0:
        discipline_id = ''
        while True:
            print_disciplines()
            if discipline_id == 0:
                print('Завершили ввод предмета у', students[student_id - 1])
                break
            discipline_id = int(input('0. Отмена\nВыберите предмет для оценки ученика ' + students[student_id - 1] + ': '))
            mark = input('Задайте отметку [12345НС]: ')
            d = disciplines[discipline_id]
            marks[students[student_id]] = { d: mark }
    else:
        print('Завершили ввод оценок у', students[student_id-1])
        break

### Ввод отметки к выбранному предмету


## Вывод журнала отметок
print(marks)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
