# 1: Using Integer
a = 5
b = 6
c = a + b

# Using Float
#Compute the area and perimeter of a circle with radius = 3
pi = 3.14
radius = 3
area = pi  * radius**2 
perimeter = 2 * pi * radius

# Integer And Float
# Change the type of the variable x to float
# Change the type of variable y to integer
x = 123446754336788543835697
y = 3.14159265358979323846
x = float(x)
y = int(y)

# Using String
# Assign foobar which gives the output shown in the last example.
# Hint: Use the triple quote as the outermost quote
foobar ='"No, thanks, Mom," I said, "I don\'t know how long it will take."'

# String And Number
# Assign 'HelloWorld!' to variable a
a = 'HelloWorld!'

# b contains 'HelloWorld!HelloWorld!HelloWorld!HelloWorld!HelloWorld!'
b = a * 5

# Number Of Characters
greeting = "Hello Google!"
# number of characters stored in the variable greeting
number_of_char = len(greeting)

# repeat the greetings based on the number of character in 'greeting'
greetings = greeting * number_of_char

# String Concatenation
# Write a function, given a string of characters, return the string together with '_'s of the same length.
def underline(title):
  return title + '\n' + len(title) * '_'
  
#   String Methods
# Use one or more string methods in above examples, extract the substring
# surrounded by 'xyz' at the beginning and end. Replace the ',' in the substring with '|'.
# and remove all trailing space.

str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
idx1 = str1.find( 'xyz'  )                    # get the position of 'xyz'
idx2 = str1.find( 'xyz'  , idx1+1)            # get the next 'xyz'
str1 = str1[idx1+3:idx2].replace( ',', '|' )    # replace ',' with '|'
str1 = str1.strip()                            # strip trailing spaces. 


# Basic Types
# Assign arbitrary values to the variables such that they are of the types used in the examples
a = 'sumon'
b = 29
c = 29.3
d = [1,2,3]

# Complex Number
# Compute the sum and product of 2 complex numbers:
# (2+3j) and (4+5j)
a = 2 + 3j
b = 4 + 5j
sum_ab = a + b
prod_ab = a * b

# String Formatting Operations
# Write a function that does a decimal to hexadecimal conversion.
# Hint: Make use of "%x" for hexadecimal format.
def dec2hex(num):
  return "0x%0.2x" % (num)

# Accessing String Elements
# Extract each word from 'greetings' and assign to 
# variables 'first', 'middle' and 'last'.
greetings = "How are you"
first  = greetings[0 :3]
middle = greetings[4 :7 ]
last   = greetings[8 : ]

# Integer (Octal And Hexadecimal)
a = 25
b = 031
c = 0x19

# Data Type


