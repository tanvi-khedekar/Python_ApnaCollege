students = ["ram", "shyam", "kishan", "radha", "radhika"]

# we want to print names only until "radha", i.e. ram to kishan

for student in students:
  if student == "radha":
    break;                      # semicolon is optional in python
  print(student)                # ram shyam kishan

for student in students:
  if student == "kishan":
    continue                  # this means run another loop, ignore this one
  print(student)