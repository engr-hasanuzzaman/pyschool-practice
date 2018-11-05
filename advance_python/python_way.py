# bad way
ages = [12, 34, 56]
index = 0
for age in ages:
  print("age is %d and index is %d" % (age, index))
  index += 1

# python way

for index, age in enumerate(ages):
  print("age is %d and index is %d" % (age, index))