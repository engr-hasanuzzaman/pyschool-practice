# Create List
## A list behaves like a container, and it is able to contain more than one value. Create a list with the values as shown in the example below.
aList = ['Hello', 0, 20.0, 'World']

# add item to list
aList = ['Hello', 0] 
aList.append(20.0)
aList.append('World')

# remove item from list
aList = ['hello', 'i', 'love', 'python', 'programming']
aList.remove('i')
aList.remove('love')
#aList.remove('love')

#Add Numbers In A List
def addNumbersInList(numbers): 
  total = 0
  for n in numbers:
    total += n
  return total

  #Add Odd Numbers In A List
  def addOddNumbers(numbers):
  total = 0
  for n in numbers:
    if n % 2 == 1: total += n
  return total

  # Count odd numbers
  def countOddNumbers(numbers):
  total = 0
  for n in numbers:
    if n % 2 == 1: total += 1
  return total
  
  # Get Even Numbers
  def getEvenNumbers(numbers):
  even_n = []
  for n in numbers:
    if n % 2 == 0: even_n.append(n)
  return even_n

  # Remove First And Last
  def removeFirstAndLast(numbers):
  if len(numbers) > 0: numbers.remove(numbers[0])
  if len(numbers) > 0:numbers.remove(numbers[-1])
  return numbers

  # Get Maximum Number
  ### Write a function getMaxNumber(numbers) that returns the maximum number in a list.
  def getMaxNumber(numbers):
  if len(numbers) == 0: return 'N.A'
  max_number = -99999
  
  for n in numbers:
    if n > max_number: max_number = n
  return max_number
   