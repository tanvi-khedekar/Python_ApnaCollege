# or (atleast 1 is true -> true)
print(2 > 3 or 2 > 1)         # true

# and (both conditions MUST be true -> true)
print(3 > 2 and 2 > 1)        # true
print(3 > 2 and 2 > 6)        # false

# not (makes true -> false, false -> true)
print(not 2 > 3)              # true
print(not 3 > 2)              # false