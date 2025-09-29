
course = "Computer Science"
char_list = list(course)
print("char_list:", char_list)
sorted_char_list = sorted(char_list)
print("sorted_char_list:", sorted_char_list)
sorted_ignore_case = sorted(char_list, key=lambda c:c .lower)
print("sorted_ignore_case:", sorted_ignore_case)
# create a list data structure of the characters from the course string
# sort the list into alphabetical order
