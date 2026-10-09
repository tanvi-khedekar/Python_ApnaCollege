marks = {95, 98, 97, 97, 97}
print(marks)                      # {97, 98, 95}     97 wont be printed as sets only consider unique values
#print(marks[0])                   # TypeError: 'set' object is not subscriptable       i.e. indexes dont exist in sets    thus called "unordered"

# so, if we wanna iterate through it, we can do so through a loop
for score in marks:
  print(score)                     # 97 98 95 (printed 1 below the other)        as it is unordered with no indexes