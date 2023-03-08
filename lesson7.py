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

# 7) #############

# my_list = [2, 4, 1, 5, 3, 7]
# count = 0
# new_list = []
# for i in my_list:
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         count += 1
#         new_list.append(my_list[i])
#
# print(new_list)

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

# 11) #####Not working as i want

my_str1 = "aaaasdf1"
my_str2 = "asdfff2"
new_str = []
for symbol in my_str1.lower():
        if symbol not in new_str:
            new_str.append(symbol)
        for symbol1 in my_str2.lower():
            if symbol1 not in new_str:
                new_str.append(symbol1)

result = new_str.intersection(new_str)




