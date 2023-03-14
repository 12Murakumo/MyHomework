# 1)

# my_list = ["oma", "ewa", "mou shiendeyrou", "pra", "klo", "mok", "par"]
# new_list = []
#
# for i in range(len(my_list)):
#     if i % 2:
#         new_list.append(my_list[i][::-1])
#     else:
#         new_list.append(my_list[i])
# print(new_list)

# 2)

# my_list = ["aak", "aak", "kar", "lom"]
# new_list = []
#
# for symbol in my_list:
#     if "a" in symbol[0::][0]:
#         new_list.append(symbol)
#
# print(new_list)

# 3)

# my_list = ["afa", "fla", "mle", "bkal"]
# new_list = []
# for newlist in my_list:
#     if "a" in newlist:
#         new_list.append(newlist)
#
# print(new_list)

# Второй вариант

# my_list = ["afa", "fla", "mle", "bkal"]
# new_list = [newlist for newlist in my_list if "a" in newlist]
# print(new_list)

# 4,a)

# Работает, но не знаю как вывести по мимо возраста имя

# person = [{
#     "first_name": "Yasuo",
#     "age": "35",
#     "adress": "Ionia",
#     },
#     {"first_name": "Riven",
#      "age": "25",
#      "adress": "Noxus",
#      },
#     {
#         "first_name": "Rudis",
#         "age": "25",
#         "adress": "league",
#     },
#     {
#         "first_name": "Paulo",
#         "age": "19",
#         "adress": "league",
#
#     },
#     {
#         "first_name": "Admin",
#         "age": "34",
#         "adress": "Riot",
#     }]
# min_age_person = []
#
# for i in person:
#     if i["age"] not in min_age_person:
#         min_age_person.append(i["age"])
#     else:
#         min_age_person.append(i["age"])
# print(min(min_age_person))


# 4, б)
# people = [{"name": "John", "age": 15},
#           {"name": "Jane", "age": 27},
#           {"name": "Jack", "age": 45},
#           {"name": "James", "age": 32},
#           {"name": "Judy", "age": 19},
#           {"name": "Jake", "age": 52}]
#
# longest_names = []
# max_length = 0
#
# for person in people:
#     name_length = len(person["name"])
#     if name_length > max_length:
#         longest_names = [person["name"]]
#         max_length = name_length
#     elif name_length == max_length:
#         longest_names.append(person["name"])
#
# print(longest_names)

# 4, в)
#
# people = [{"name": "John", "age": 15},
#           {"name": "Jane", "age": 27},
#           {"name": "Jack", "age": 45},
#           {"name": "James", "age": 32},
#           {"name": "Judy", "age": 19},
#           {"name": "Jake", "age": 52}]
#
# total_age = 0
# num_people = len(people)
#
# for person in people:
#     total_age += person["age"]
#
# average_age = total_age / num_people
#
# print(average_age)

# 5,а

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# keys_1 = set(my_dict_1.keys())
# keys_2 = set(my_dict_2.keys())
#
# common_keys = list(keys_1 & keys_2)
# print(common_keys)

# 5,б

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# keys_1 = set(my_dict_1.keys())
# keys_2 = set(my_dict_2.keys())
#
# unique_keys = list(keys_1 - keys_2)
# print(unique_keys)

# 5, в

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# unique_keys = set(my_dict_1.keys()) - set(my_dict_2.keys())
# new_dict = {key: my_dict_1[key] for key in unique_keys}
# print(new_dict)

# 5, г

# my_dict_1 = {'a': 1, 'b': 2, 'c': 3}
# my_dict_2 = {'b': 4, 'c': 5, 'd': 6}
# new_dict = {}  # створюємо пустий словник
#
# for key in set(my_dict_1.keys()) | set(my_dict_2.keys()):  # об'єднуємо ключі з двох словників
#     if key in my_dict_1 and key not in my_dict_2:  # якщо ключ є тільки в першому словнику
#         new_dict[key] = my_dict_1[key]
#     elif key in my_dict_2 and key not in my_dict_1:  # якщо ключ є тільки в другому словнику
#         new_dict[key] = my_dict_2[key]
#     else:  # якщо ключ є в обох словниках
#         new_dict[key] = [my_dict_1[key], my_dict_2[key]]
#
# print(new_dict)
