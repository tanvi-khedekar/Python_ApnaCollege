#print(1)
#print(2)
#print(3)
#print(4)
#print(5)

# loops to minimize this

# while loop
i = 1

#while i <= 500:
 # print(i)
  #i = i + 1             # not having this will result in an INFINITE LOOP
  #i = i + 1

while i <= 5:                    # this will create the star pattern starting with 1 star(*) to 5 stars(*****)
  print(i * "*")
  i = i + 1

while i >= 0:                    # this will create the star pattern starting with 5 stars(*****) to 1 star(*)
  print(i * "*")
  i = i - 1