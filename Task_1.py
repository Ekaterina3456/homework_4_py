# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.


def sum_num(num: str):
    summa = 0
    for i in num:
        summa += int(i)
    return summa


def min_num(num: str):
    minimum = 10
    for i in num:
        if int(i) < minimum:
            minimum = int(i)
    return minimum


def max_num(num: str):
    maximum = 0
    for i in num:
        if int(i) > maximum:
            maximum = int(i)
    return maximum


number = input('введите число ')

while True:
    action = int(input('Выбирите действие:\n'
                       '\t1. вывести сумму чисел\n'
                       "\t2. найти минимальное число\n"
                       "\t3. найти максимальное число\n"
                       '\t4. выйти\n'))

    match action:
        case 1:
            print(sum_num(number))
        case 2:
            print(min_num(number))
        case 3:
            print(max_num(number))
        case 4:
            break
