old_age = input("enter your old age: ")

#new_age = old_age + 2         #TypeError: can only concatenate str (not "int") to str
new_age = int(old_age) + 2      #Typecasting, converted oldage string into integer with int()
print(new_age)

number = 18
print(float(number))      #converted number into decimal/floating point number -> 18.0


# CODE TO PRINT SUM OF 2 NUMBERS

first = input("enter first number: ")
second = input("enter second number: ")

sum = first + second
print(sum)        #this prints 3+2=32 as it concatenates 2 strings 3&2

sum = int(first) + int(second)
#print("the sum is:" + sum)      #TypeError: can only concatenate str (not "int") to str
print("the sum is:" + str(sum))