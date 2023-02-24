def convert():
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
    #Если в момент выбора операции с числами выбрано неверное значение
        else:
            print("Ошибка ввода данных")
            convert()

        print(f"Результат: {result}")
    #Если введена строка вместо цифр
    except:
        print("Ошибка ввода данных")
        convert()
#Для возможности продолжить работу программы, но по своему желанию
convert()
while True:
    flag = input("Еще раз?[да/нет]")

    if flag == 'да':
        convert()
    else:
        quit("bye")
