# #my_str = input("Input text please: ")
# #unique_list = []
# #for x in my_str.lower():
#  #   if x not in unique_list:
#  #       unique_list.append(x)
# #print(len(unique_list))
#
# #my_str = "bla BLA car"
# #value_list = []
#
# #result = 0
#
# #for x in my_str.lower():
#  #   if x not in value_list:
#  #       value_list.append(x)
# #result = len(value_list)
# #print(result)
#
# # my_str = "bla BLA car"
# # new_list = list(my_str[::2])
# # print(new_list)
#
# s = "22132sdaasas2//:-."
# print (''.join(sorted([n for n in set(s) if n.isdigit()], reverse=True)))

# value = "1005000"
# count = 0
# print(value[:len(value)-1])
# value = random.randrange(1000, 10000)
# print(value)

# count = 0
# print(value[0:7])


# print(value[:len(value)-1])
# while True:
#      if value[-1] == '0':
#          count +=1
#          value = value[:len(value) - 1]
#
#      else:
#          break
#
# print(count)

#NOT WORKING
# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# count = 0
# for i in my_list:
#     if i == my_list[1] > (my_list[0] + my_list[2]):
#         count += 1
#         if i == my_list[3] > (my_list[1] + my_list[4]):
#             count += 1
#             if i == my_list[5] > (my_list[4] + my_list[6]):
#                 count += 1
#                 count = list(count)
#             else:
#                 break
# print(count)

#NOT WORKING
# for i in str(value):
#     start = (start.count('0'))
#     if not '0' in str(value):
#         print(value)

#Сосчитать количество цифр в строке

# my_list = "43 більше ніж 34, але меньше ніж 56"
# count = 0
# result = 0
# for i in my_list:
#     if i.isdigit():
#         count += 1
#     if not i.isdigit():
#         pass
# print(count)

#NOW WORKING
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# count = 0
# for i in my_list:
#     if my_list[1] == int:
#         count += 1
#     else:
#         break
# print(count)

#METOD SUM
# value = [10, 10]
# result = sum(value)
# print(result)

# Найти уникальные символы, которые встречаются как в 1, так и 2 варианте лишь единожды:

# my_str1 = "aaaasdf1"
# my_str2 = "asdfff2"
# new_str = []
# for symbol in my_str1.lower():
#         if symbol not in new_str:
#             new_str.append(symbol)
#         for symbol1 in my_str2.lower():
#             if symbol1 not in new_str:
#                 new_str.append(symbol1)
#
# print(new_str)