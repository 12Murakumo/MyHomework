 #Хотел сделать цикличным программу через - "while True:, break"
 #Но сейчас нет времени чтобы разобраться в причине неверного выполнения команды.
result = 0
try:
    value_1 = float(input("Введите первое число: "))
    value_2 = float(input("Введите второе число: "))

    operation = input("Выберите одну из операций: ('+', '-', '*', '/')\n")
    if operation == '+':
        result = value_1 + value_2
        print('Ответ: ')
    elif operation == '-':
        result = value_1 - value_2
        print('Ответ: ')
    elif operation == '*':
        result = value_1 * value_2
        print('Ответ: ')
    elif operation == '/':
        result = value_1 / value_2

    print(result)

except ValueError:
    quit("Ошибка ввода данных")
except ZeroDivisionError:
    quit("Не дели меня на ноль")