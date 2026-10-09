# IN-BUILT FUNCTIONS -> int(), str(), bool()

# MODULE FUNCTIONS -> when related functions and related variables are stored inside one file, it is called a MODULE in python

#import math                          # takes entire module into our code
#print(dir(math))                      # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# if we want only a particular function from this 'math' module, 

#from math import sqrt                 # takes only 'sqrt' which is a function that returns the square root of any given number, into our code
#print(sqrt(4))                        # 2.0
#print(sqrt(16))                       # 4.0

#from math import *                     # this will import all functions from the 'math' maodule, so we can directly use the 'sqrt' function
#print(sqrt(25))                        # 5.0

# USER-DEFINED FUNCTIONS
def print_sum(first, second=4):             # default for second will be 4, i.e. if nothing is passed, python will consider 4 for it
  print(first + second)

print_sum(1, 2)                       # calling the function, executing it, running it     o/p: 3
print_sum(1)                          # o/p: 5      as python will consider 4 as we have not passed the 'second' parameter