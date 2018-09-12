# 1: Add Two Numbers
def addNumber(x, y):
  return x + y

# Subtract Numbers
def subtractNumber(x, y): 
  return x - y

# Integer And Float
# Change the type of the variable x to float
# Change the type of variable y to integer
x = 123446754336788543835697
y = 3.14159265358979323846
x = float(x)
y = int(y)

# Bigger Number
def getBiggerNumber(n, m):
  return n if n > m else m

# Using Math Functions
import math
# Calculate the square root of 16 and stores it in the variable a
a = math.sqrt(16)

# Calculate 3 to the power of 5 and stores it in the variable b
b = math.pow(3, 5)

# Calculate area of circle with radius = 3.0 by making use of the math.pi constant and store it in the variable c
c = math.pi * 3.0 * 3.0

# Celsius To Fahrenheit Conversion
# Note: Return a string of 2 decimal places.
def Cel2Fah(temp): 
  return "%.2f" % (temp * 9.0 / 5 + 32)

# Body Mass Index (BMI) Calculator
# Note: Return a string of 1 decimal place.
def BMI(weight, height):
  return "%0.1f" % (float(weight) / (height * height))

# Percentage Calculation
def percent(n, t):
  return int(float(n) / t * 100)
