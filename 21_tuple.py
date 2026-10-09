# tuples cannot be modified like lists(append, insert, etc.). they are immutable

marks = (95, 98, 97, 97, 97)            # these ()parenthesis are not necessary, but use them for better code readability
#marks[0] = 99                     # TypeError: 'tuple' object does not support item assignment

# operations on tuples

print(marks.count(97))              # 3 (counts how many times an object is seen)
print(marks.index(97))              # 2 (seen at index 2 for the first time, so returns 2)

