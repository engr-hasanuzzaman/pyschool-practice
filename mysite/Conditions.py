# Determina A Even Number
  def isEven(x): 
	return x % 2 == 0

# Checking Isosceles Triangle
def isIsosceles(x, y, z): 
	if(x <= 0 or y <= 0 or z <= 0): return False
	
	return x == y or y == z or x == z

# Checking Scalene Triangle
def isScalene(x, y, z):
	if(x == y or y == z or x == z): return False
	return True 

# Fitness Standard
def Fitness(a, b, c):
	sum = a + b + c
	if(a >= 4 and b >= 4 and c >= 4 and sum >= 13):
		return 'Gold'
	elif(a >= 3 and b >= 3 and c >= 3 and sum >= 10):
		return 'Silver'
	elif(a >= 2 and b >= 2 and c >= 2 and sum >= 7):
		return 'Pass'
	else:
		return 'Fail'

# Prime Number
# Hint: Step through the range between (2, number-1), 
# and determine if the number is divisible using the modulus operator.
def isPrime(x):
	if(x < 2): return False
	
	for i in range(2, x - 1):
		if(x % i == 0): return False
	return True

# Health Risk Asessment
def HealthScreen(weight, height):
	bmi = weight / height ** 2
	if(bmi >= 27.5): return 'Your BMI is %.1f (High Risk).'%(bmi)
	elif(bmi >= 23): return 'Your BMI is %.1f (Moderate Risk).'%(bmi)
	elif(bmi >= 18.5): return 'Your BMI is %.1f (Low Risk).'%(bmi)
	else: return 'Your BMI is %.1f (Risk of nutritional deficiency diseases).'%(bmi)

# Is Triangle
def isTriangle(x,y,z):
	if((x + y) > z and (y + z) > x and (x + z) > y): return True
	return False

