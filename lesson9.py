# 1
# def process_strings(my_list):
#     new_list = []
#
#     for index, string in enumerate(my_list):
#         if index % 2 == 0:  # парне місце
#             new_list.append(string)
#         else:  # непарне місце
#             new_list.append(string[::-1])
#
#     return new_list
#
#
# # Тестові дані
# my_list = ["один", "два", "три", "чотири", "п'ять"]
#
# # Виклик функції
# result = process_strings(my_list)
#
# # Вивід результату
#  print(result)

# 2

# def filter_by_first_letter(my_list):
#     new_list = []
#
#     for string in my_list:
#         if string[0].lower() == 'a':
#             new_list.append(string)
#
#     return new_list
#
# # Тестові дані
# my_list = ["apple", "banana", "avocado", "grape", "apr"]
#
# # Виклик функції
# result = filter_by_first_letter(my_list)
#
# # Вивід результату
# print(result)

# 3)

# def filter_by_letter_a(my_list):
#     new_list = []
#
#     for string in my_list:
#         if 'a' in string.lower():
#             new_list.append(string)
#
#     return new_list
#
# # Тестові дані
# my_list = ["apple", "banana", "Avocado", "grape", "Apricot"]
#
# # Виклик функції
# result = filter_by_letter_a(my_list)
#
# # Вивід результату
# print(result)

# 4)

# def filter_strings(my_list):
#     new_list = []
#
#     for item in my_list:
#         if isinstance(item, str):
#             new_list.append(item)
#
#     return new_list
#
# # Тестові дані
# my_list = ["apple", 42, "banana", 7, "grape", "Apricot", 12]
#
# # Виклик функції
# result = filter_strings(my_list)
#
# # Вивід результату
# print(result)

# 5)

# def unique_chars(my_str):
#     new_list = []
#
#     for char in my_str:
#         if my_str.count(char) == 1:
#             new_list.append(char)
#
#     return new_list
#
# # Тестові дані
# my_str = "aabccdefggh"
#
# # Виклик функції
# result = unique_chars(my_str)
#
# # Вивід результату
# print(result)

# 6)

# def common_chars(str1, str2):
#     new_list = []
#
#     for char in set(str1):
#         if char in str2:
#             new_list.append(char)
#
#     return new_list
#
# # Тестові дані
# str1 = "apple"
# str2 = "pineapple"
#
# # Виклик функції
# result = common_chars(str1, str2)
#
# # Вивід результату
# print(result)

# 7)

# def unique_common_chars(str1, str2):
#     new_list = []
#
#     for char in set(str1):
#         if char in str2 and str1.count(char) == 1 and str2.count(char) == 1:
#             new_list.append(char)
#
#     return new_list
#
# # Тестові дані
# str1 = "apple"
# str2 = "pineapple"
#
# # Виклик функції
# result = unique_common_chars(str1, str2)
#
# # Вивід результату
# print(result)

# 8)

# import random
# import string
#
# def generate_email(names, domains):
#     name = random.choice(names)
#     domain = random.choice(domains)
#     random_number = random.randint(100, 999)
#     random_string_length = random.randint(5, 7)
#     random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
#
#     email = f"{name}.{random_number}@{random_string}.{domain}"
#     return email
#
# # Тестові дані
# names = ["ivan", "petro", "olga", "sophia", "vitaliy"]
# domains = ["com", "org", "net", "ua", "gov"]
#
# # Виклик функції
# generated_email = generate_email(names, domains)
#
# # Вивід результату
# print(generated_email)
