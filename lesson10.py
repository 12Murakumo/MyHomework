# 1)

# def read_domains(filename):
#     domains = []
#
#     with open(filename, "r") as file:
#         for line in file:
#             domain = line.strip().replace(".", "")
#             domains.append(domain)
#
#     return domains
#
# # Тестові дані
# filename = "domains.txt"
#
# # Виклик функції
# domains_list = read_domains(filename)
#
# # Вивід результату
# print(domains_list)

# 2)

# def read_surnames(filename):
#     surnames = []
#
#     with open(filename, "r") as file:
#         for line in file:
#             data = line.strip().split("\t")
#             if data[0] != "":
#                 surname = data[1]
#                 surnames.append(surname)
#
#     return surnames
#
# # Тестові дані
# filename = "names.txt"
#
# # Виклик функції
# surnames_list = read_surnames(filename)
#
# # Вивід результату
# print(surnames_list)

# 3)

# import re
#
# def read_dates(filename):
#     date_pattern = re.compile(r"\b\d{1,2}(?:st|nd|rd|th) [A-Z][a-z]+ \d{4}\b")
#     dates_list = []
#
#     with open(filename, "r") as file:
#         for line in file:
#             match = date_pattern.search(line)
#             if match:
#                 date = match.group()
#                 dates_list.append({"date": date})
#
#     return dates_list
#
# # Тестові дані
# filename = "authors.txt"
#
# # Виклик функції
# dates_list = read_dates(filename)
#
# # Вивід результату
# print(dates_list)

# 4)

# import re
# import os
# from datetime import datetime
#
# def read_dates(filename):
#     dates = []
#
#     with open(filename, "r") as file:
#         for line in file:
#             data = line.split(",")
#             date_original = data[1].strip()
#
#             # Видаляємо порядкові суфікси
#             date_clean = re.sub(r'(\d)(st|nd|rd|th)', r'\1', date_original)
#
#             date_obj = datetime.strptime(date_clean, "%d %B %Y")  # конвертуємо в формат datetime
#             date_modified = date_obj.strftime("%d/%m/%Y")  # конвертуємо в новий формат
#
#             dates.append({"date_original": date_original, "date_modified": date_modified})
#
#     return dates
#
# # Тестові дані
# filename = "authors.txt"
#
# # Виклик функції
# dates_list = read_dates(filename)
#
# # Вивід результату
# for date_dict in dates_list:
#     print(date_dict)





