 #Хотел сделать цикличным программу через - "while True:, break"
 #Но сейчас нет времени чтобы разобраться в причине неверного выполнения команды.

try:
    value_1 = float(input("Введите первое число: "))
    value_2 = float(input("Введите второе число: "))
    result = 0
    operation = input("Выберите одну из операций: ('+', '-', '*', '/')\n")

    if operation == '+':
        result = value_1 + value_2

    elif operation == '-':
        result = value_1 - value_2

    elif operation == '*':
        result = value_1 * value_2

    elif operation == '/':
        result = value_1 / value_2
    else:
        quit("Ошибка ввода данных")

    print(f"Результат: {result}")

except:
    quit("Ошибка ввода данных")