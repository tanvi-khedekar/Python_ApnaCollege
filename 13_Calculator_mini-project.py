first = input("enter first number: ")
operator = input("enter operator (+, -, *, /, %): ")
second = input("enter second number: ")

first = int(first)                  # typecasting string to number(integer)
second = int(second)

if operator == "+":
  print(first + second)
elif operator == "-":
  print(first - second)
elif operator == "*":
  print(first * second)
elif operator == "/":
  print(first / second)
elif operator == "%":
  print(first % second)
else:
  print("Invalid operator.")