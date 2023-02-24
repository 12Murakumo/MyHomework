import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()
result = 0
while True:
    try:
        print(Fore.YELLOW)
        expr = input("Введите математическое выражение: ")
        result = numexpr.evaluate(expr)
        print(Fore.GREEN)
        print(f"Результат: {result}")
    except:
        print(Fore.RED)
        print("Ошибка ввода данных")
        print(Fore.RED)
    flag = input("Желаете продолжить? да, нет: ")
    if not flag == "да":
        quit("Bye")


