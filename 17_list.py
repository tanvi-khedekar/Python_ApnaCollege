# this is a datatype
# a complex datatype
# in this we can store multiple primitive datatypes together, it is a collectin of items

marks = [95, 98, 97]
print(marks)              # [95, 98, 97]
print(marks[0])           # 95
print(marks[1])           # 98
print(marks[-1])          # -1 index -> prints from the last item in the list(97)
print(marks[-2])          # 98
#print(marks[-4])          # IndexError: list index out of range

print(marks[0:2])         # [95, 98] (last index does not get included)
print(marks[1:3])         # [98, 97]