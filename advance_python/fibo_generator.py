def fibo():
  x, y = 1, 0
  while True:
    yield x
    y, x = x, x + y

fGen = fibo()
for i in range(10):
  print("Next fibonacci num is {}".format(next(fGen)))    