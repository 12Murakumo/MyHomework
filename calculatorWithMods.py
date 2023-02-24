import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()
result = 0
while True:
    try:
        expr = input("Введите математическое выражение: ")
        result = numexpr.evaluate(expr)
    except:
        quit("Ошибка ввода данных")

    print(Fore.YELLOW)
    print(f"Результат: {result}")
    #Просто через While True, без break и тд., потому что калькулятору и так будет нормально работать в приложении