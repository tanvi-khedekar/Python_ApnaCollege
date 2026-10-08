name = "Tony Stark"

print(name.upper())       # uppper() is a method to convert string to all capital letters
print(name)               # it does not change/convert the original string

print(name.lower())       # o/p: tony stark

# find operation
print(name.find('S'))       # returns index: 5
print(name.find('s'))       # o/p:-1      means it was not found
print(name.find('stark'))   # o/p: -1
print(name.find('Stark'))   # o/p: 5

# replace operation
print(name.replace("Tony Stark", "Ironman"))          # Ironman
print(name)                                           # Tony Stark
print(name.replace("Stark", "Ironman"))               # Tony Ironman
print(name.replace("T", "G"))                         # Gony Stark

