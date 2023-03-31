#!/bin/python3

#from pprint import pprint

disciplines = {
    1: 'Математика',
    2: 'Чтение',
    3: 'Прописи',
    4: 'Физкультура'
}

marks = {}
students = ['Иванов Вася']
marks[students[-1]] = {}

### пример вывода значений словаря
#print("\n".join(disciplines.values()))

## Цикл ввода имён
while True:
    name = input('Введите имя ученика, 0 для отмены: ')
    if name != '0':
        students.append(name)
        marks[students[-1]] = {}
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
        
def print_marks():
    print('\nСодержимое журнала:')
    for s in students:
        print(s + ':')
        for d in marks[s]:
            print(' - ' + d + '\t' + marks[s][d])
            
    #pprint(marks)

## Цикл ввода отметок с выбором ученика
while True:
    print_students()
    
    try:
        student_id = int(input('0. Завершение\nВыберите ученика: '))
    except ValueError:
        continue
        
    if student_id > len(students):
        continue
    
    if student_id != 0:
        discipline_id = ''
        while True:
            print_disciplines()
            discipline_id = int(input('0. Отмена\nВыберите предмет для оценки ученика ' + students[student_id - 1] + ': '))
            if discipline_id == 0:
                print('Завершили ввод предмета у', students[student_id - 1])
                break
            mark = input('Задайте отметку [12345НС]: ')
            d = disciplines[discipline_id]
            marks[students[student_id - 1]][disciplines[discipline_id]] = mark
    else:
        print('Завершили ввод оценок у', students[student_id - 1])
        break

### Ввод отметки к выбранному предмету


## Вывод журнала отметок
print_marks()