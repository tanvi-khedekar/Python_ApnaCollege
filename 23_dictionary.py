# we store key-value pairs in a dictionary

marks = {"english" : 95, "chemistry" : 98}
print(marks["chemistry"])                         # 98

# adding new marks
marks["physics"] = 97
print(marks)                                      # {'english': 95, 'chemistry': 98, 'physics': 97}

marks["physics"] = 99                             # changing the physics marks
print(marks)                                      # {'english': 95, 'chemistry': 98, 'physics': 99}

#information = {"ram" : "balkishan"}