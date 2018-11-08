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