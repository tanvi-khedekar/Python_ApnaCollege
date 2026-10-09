age = 2

# importance of INDENTATION!
if age >= 18:                         # starting condition               
  print("you are an adult")                 
  print("you can vote")
elif age < 18 and age > 3:                # if starting condition is not true, check this
  print("you are in school")
else:                                 # age is less than or equal to 3, if none of the above conditions are true it reaches here
  print("you are a child")

print("thank you")                    # this will always print as it is outside the if scope, irrespective of the conditions