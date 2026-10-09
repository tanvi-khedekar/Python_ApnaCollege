marks = [95, 98, 97]

marks.append(99)              # appends value to the endof the list
print(marks)                  # [95, 98, 97, 99]

marks.insert(0, 99)
print(marks)                  # [99, 95, 98, 97, 99]

print(99 in marks)            # True, the 'in' keyword checks if '99' exists in 'marks'
print(93 in marks)            # False

print(len(marks))             # 5, 'len' returns the number of values in the list


# iterating through the list using 'while' loop

i = 0
while i < len(marks):
  print(marks[i])
  i = i + 1

marks.clear()
print(marks)                # []