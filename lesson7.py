# 1)

# value = 1005000
# start = str(value)
# result = (start.count('0'))
# print(int(result))

# 2)
#
# value = "1005000"
# val = list(value)
# val.reverse()
# count = 0
# for i in val:
#     if i == '0':
#         count +=1
#     else:
#         break
# print(count)

# 3)

# my_list1 = 'asdfgj'
# my_list2 = 'poiytr'
# my_result = []
# my_result.append(my_list1[::2])
# my_result.append(my_list2[::2])
# print(my_result)

# 4)

# my_list = [5, 3, 1, 3]
# new_list = my_list[1::]
# new_list.append(my_list[0])
# print(new_list)

# 5)

# my_list = [1, 2, 3, 4]
# val1 = my_list[0]
# val = my_list.pop(0)
# my_list.append(val1)
# print(my_list)


# 6)

# my_list = '43 більше ніж 34, але меньше ніж 56'
# numbers = []
# count = ""
#
# for i in my_list:
#     if i.isdigit():
#         count += i
#     else:
#         if count.isdigit():
#             numbers.append(int(count))
#             count = ""
# if count != "":
#     numbers.append(int(count))
#
# print(sum(numbers))

# 7)

# my_list = [2, 4, 1, 5, 3, 7, 2, 1]
# # пустой список (list), сюда будут вкладываться элементы полученные циклом for
# new_list = []
# # Начало цикла, обьявление условия, определение границ для работы цикла
# for i in range(1, len(my_list) - 1):
#     # первое условие: Если значение my_list[i] больше суммы его соседей (my_list[i -1] + my_list[i -1])
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         # То добавляем через метод append это значение в пустой список new_list
#         new_list.append(my_list[i])
#
# # Выписываем результат, а именно те символы что были помещены в new_list через .append. А чтобы получить их количество
# # запрашиваемое условием задачи - принтим его как перечень с использованием len. В таком случае вывод на экране будет не
# # [4, 5, 7], а 3, что и есть верно
# print(len(new_list))

# 8)

# my_list = [1, 2, 3, '11', '22', 33]
# new_list = []
# count = ""
#
# for i in my_list:
#     if type(i) == int:
#         count += str(i)
#     else:
#         if count.isdigit():
#             new_list.append(count)
#             count = ""
# if count != "":
#     new_list.append(count)
#
# print(new_list)

# 9)

# my_str = "Bla BLA car"
# new_list = []
#
# for x in my_str.lower():
#     if x not in new_list:
#         new_list.append(x)
#
# print(new_list)

# 10)

# my_str1 = "Bla BLA car"
# my_str2 = "Blc HLA mar"
# new_str = []
# for x in my_str1.lower():
#     if x not in new_str:
#         new_str.append(x)
#         for x in my_str2.lower():
#             if x not in new_str:
#                 new_str.append(x)
#
# print(new_str)

# 11)
#
# my_str1 = "aaaasdf1"
# my_str2 = "asdfff2"
#   # два пустых списка (list), в которые будут помещаться найденые элементы в цикле
# new_str1 = []
# new_str2 = []
# for symbol in my_str1:
#     # С помощью метода str.count ищем количество вхождений подстроки в строке. Конкретный символ не указан, но задано
#     # количество допустимых вхождений " == 1 ", а значит цикл будет искать уникальный символ, который встречается лишь
#     # единожды в указанной строке
#     if my_str1.count(symbol) == 1:
#         new_str1.append(symbol)
#     for symbol1 in my_str2:
#         # Ту же операцию совершаем для my_str2
#         if my_str2.count(symbol1) == 1:
#             new_str2.append(symbol1)
#
# # Теперь нужно обьеденить два списка new_str1 и new_str2 в которые помещены результаты из строк my_str1 и my_str2.
# # обозначаем новые переменные, с значением new_str1 и new_str2, но переведенные в set, для работы метода intersection
# # Этим методом находим и оставляем только уникальные символы в строке, которые встречаются в обеих строках
# val_set_1 = set(new_str1)
# val_set_2 = set(new_str2)
# result = val_set_1.intersection(val_set_2)
# print(result)


