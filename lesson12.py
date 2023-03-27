# 1)

# import re
# import os
# from datetime import datetime
#
# class DateExtractor:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def read_dates(self):
#         dates = []
#
#         with open(self.file_name, "r") as file:
#             for line in file:
#                 date_match = re.search(r'(\d+)?(?:st|nd|rd|th)? (\w+) (\d+)', line)
#
#                 if date_match:
#                     date_original = date_match.group(0)
#                     day = date_match.group(1)
#                     month = date_match.group(2)
#                     year = date_match.group(3)
#                 else:
#                     month_year_match = re.search(r'(\w+) (\d+)', line)
#                     if month_year_match:
#                         date_original = month_year_match.group(0)
#                         day = None
#                         month = month_year_match.group(1)
#                         year = month_year_match.group(2)
#                     else:
#                         continue
#
#                 date_clean = f'{day or "1"} {month} {year}'
#
#                 try:
#                     date_obj = datetime.strptime(date_clean, "%d %B %Y")
#                     if day:
#                         date_modified = date_obj.strftime("%d/%m/%Y")
#                     else:
#                         date_modified = date_obj.strftime("%m/%Y")
#
#                     dates.append({"date_original": date_original, "date_modified": date_modified})
#                 except ValueError:
#                     continue
#
#         return dates
#
# # Тестування класу
# date_extractor = DateExtractor("authors.txt")
# dates = date_extractor.read_dates()
# print(dates)

# 2)

# import re
# import os
# from datetime import datetime
#
#
# class DateExtractor:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.dates_as_strings = []
#
#     def read_dates(self):
#         dates = []
#
#         with open(self.file_name, "r") as file:
#             for line in file:
#                 date_match = re.search(r'(\d+)?(?:st|nd|rd|th)? (\w+) (\d+)', line)
#
#                 if date_match:
#                     date_original = date_match.group(0)
#                     day = date_match.group(1)
#                     month = date_match.group(2)
#                     year = date_match.group(3)
#                 else:
#                     month_year_match = re.search(r'(\w+) (\d+)', line)
#                     if month_year_match:
#                         date_original = month_year_match.group(0)
#                         day = None
#                         month = month_year_match.group(1)
#                         year = month_year_match.group(2)
#                     else:
#                         continue
#
#                 date_clean = f'{day or "1"} {month} {year}'
#
#                 try:
#                     date_obj = datetime.strptime(date_clean, "%d %B %Y")
#                     if day:
#                         date_modified = date_obj.strftime("%d/%m/%Y")
#                     else:
#                         date_modified = date_obj.strftime("%m/%Y")
#
#                     dates.append({"date_original": date_original, "date_modified": date_modified})
#                 except ValueError:
#                     continue
#
#         return dates
#
#     def get_dates_as_strings(self):
#         dates = self.read_dates()
#         for date in dates:
#             date_str = date['date_modified'].replace('.', '')
#             self.dates_as_strings.append(date_str)
#         return self.dates_as_strings
#
#
# # Тестування класу
# date_extractor = DateExtractor("authors.txt")
# dates_as_strings = date_extractor.get_dates_as_strings()
# print(dates_as_strings)

# 3)

# class FileDataExtractor:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def get_surnames(self):
#         surnames = []
#
#         with open(self.file_name, "r") as file:
#             for line in file:
#                 data = line.strip().split("\t")
#                 if data[0] != "":
#                     surname = data[1]
#                     surnames.append(surname)
#
#         return surnames
#
# # Тестування класу
# file_data_extractor = FileDataExtractor("names.txt")
# surnames_list = file_data_extractor.get_surnames()
#
# # Вивід результату
# print(surnames_list)

# 4)

import re
from datetime import datetime

class DateExtractor:
    def __init__(self, filename):
        self.filename = filename

    def read_dates(self):
        dates = []

        with open(self.filename, "r") as file:
            for line in file:
                date_match = re.search(r'(\d+)?(?:st|nd|rd|th)? (\w+) (\d+)', line)

                if date_match:
                    date_original = date_match.group(0)
                    dates.append({"date": date_original})

        return dates

# Тестові дані
filename = "authors.txt"

# Створення об'єкту класу DateExtractor
date_extractor = DateExtractor(filename)

# Виклик методу read_dates
dates_list = date_extractor.read_dates()

# Вивід результату
for date_dict in dates_list:
    print(date_dict)

