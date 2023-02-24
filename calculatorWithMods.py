import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()
result = 0
while True:
    try:
        expr = input("Введите математическое выражение: ")
        result = numexpr.evaluate(expr)
        print(Fore.YELLOW)
        print(f"Результат: {result}")
    except:
        print("Ошибка ввода данных")
    flag = input("Желаете продолжить? да, нет")
    if not flag == "да":
        quit("Bye")


