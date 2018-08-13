# 1: Add Two Numbers
def addNumber(x, y):
  return x + y

# 2: Subtract Numbers
def subtractNumber(x, y): 
  return x - y

# 3: Bigger Number
def getBiggerNumber(n, m):
  return n if n > m else m

# 4: Using Math Functions
import math
# Calculate the square root of 16 and stores it in the variable a
a = math.sqrt(16)

# Calculate 3 to the power of 5 and stores it in the variable b
b = math.pow(3, 5)

# Calculate area of circle with radius = 3.0 by making use of the math.pi constant and store it in the variable c
c = math.pi * 3.0 * 3.0

# 5: Celsius To Fahrenheit Conversion
# Note: Return a string of 2 decimal places.
def Cel2Fah(temp): 
  return "%.2f" % (temp * 9.0 / 5 + 32)

# 6: Body Mass Index (BMI) Calculator
# Note: Return a string of 1 decimal place.
def BMI(weight, height):
  return "%0.1f" % (float(weight) / (height * height))

# 7: Percentage Calculation
def percent(n, t):
  return int(float(n) / t * 100)

# 8: Pythagoras' Theorem
# Hint: You can use math.sqrt(x) to compute the square root of x.
import math
def hypotenuse(a, b):
  return math.sqrt(math.pow(a, 2) + math.pow(b,2))

# 9: Sum Of Last Digits
def getSumOfLastDigits(numList):
  sum = 0
  for n in numList:
    sum += n % 10
  return sum  

# 10: Introduce Yourself
def introduce(name, age=0):
    msg = "My name is %s. " % name
    if age == 0:
       msg += "My age is secret."
    else:
       msg += "I am %d years old." % age
    return msg 