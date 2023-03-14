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

# 4, b)

person = [{
    "first_name": "Yasuo",
    "age": "35",
    "adress": "Ionia",
    },
    {"first_name": "Riven",
     "age": "25",
     "adress": "Noxus",
     },
    {
        "first_name": "Rud",
        "age": "25",
        "adress": "league",
    },
    {
        "first_name": "Puto",
        "age": "19",
        "adress": "league",

    },
    {
        "first_name": "Axe",
        "age": "34",
        "adress": "Riot",
    }]

person_name_list = []
for key, value in {person.items()}:
    print(key, value)
# for i in person:
#     if i["first_name"] not in person_name_list:
#         person_name_list.append(i["first_name"])
#     else:
#         break
# print(max(person_name_list))

