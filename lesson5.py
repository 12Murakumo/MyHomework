# 1)a

# my_str = "python12"
# print(my_str[2])

# 1)b

# my_str = "python12"
# print(my_str[-2])

# 1)c

# my_str = "python12"
# print(my_str[0:5])

# 1)d

# my_str = "python12"
# print(my_str[0:-2])

# 1)e

# my_str = "pytnon12"
# print(my_str[::2])

# 1)f

# my_str = "python12"
# print(my_str[1::2])

# 1)g

# my_str = "python12"
# print(my_str[::-1])

# 1)h

# my_str = "python12"
# print(my_str[::-2])

# 1)i

# my_str = "python12"
# print(len(my_str))

# 2)

# my_str = "Trying to learn"
# my_str = (my_str.count(' ')+1)
# print(my_str)



# 3)

# my_string = "Ohnchoch Gochs"
# start = -1
# count = 0

# while True:
#   start = my_string.find("ch", start+1)
#   if start == -1:
#       break
#   count += 1

# print(count)


# 11)

#value1 = "hhhhh"
#value1.find("h")
#value1.rfind("h")
#value1.replace("h", "H")
#print(value1)


new_str = "hhhhhh"
first = new_str.find('h')
last = new_str.rfind('h')
my_str = new_str[0:first+1] + new_str[first+1:last].replace('h', 'H') + new_str[last:]
print(my_str)


