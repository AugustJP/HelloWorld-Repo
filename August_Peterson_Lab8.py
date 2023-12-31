"""
August Peterson
Lab 8
Functions and List review
"""




#Problem 1
'''
def calc_toll(hour, is_morning, is_weekend):
	cost = 0
	if is_weekend == True:
		if is_morning == True:
			if hour < 7:
				cost = 1.05
			else:
				cost = 2.15
		elif hour < 8:
			cost = 2.15
		else:
			cost = 1.10
	else:
		if is_morning == True:
			if hour < 7:
				cost = 1.15
			elif hour < 10:
				cost = 2.95
			else:
				cost = 1.90
		else:
			if hour < 3:
				cost = 1.90
			elif hour < 8:
				cost = 3.95
			else:
				cost = 1.40
	return cost
'''			
	
	
	  

#Problem 2
'''
def LCM(num1, num2):
	bigNum = 0

	if num1 > num2:
		bigNum = num2
		while bigNum <= num1 * num2:
			if bigNum % num1 == 0 and bigNum % num2 == 0:
				print(f'lcm = {bigNum}')
				break
			else:
				bigNum += 1
	else:
		bigNum = num2
		while bigNum <= num1 * num2:
			if bigNum % num1 == 0 and bigNum % num2 == 0:
				print(f'lcm = {bigNum}')
				break
			else:
				bigNum += 1

	return bigNum
'''


		

#Problem 3


def factorial(num):
	f = 1
	if num >= 1:
		for i in range(1, num + 1):
			f = f * i
		
	return f

def combination(m, k):
	c = factorial(m) / (factorial(k) * factorial(m - k))
	
	return c



if __name__ == '__main__':
	'''
	#print(calc_toll(8, True, False))  #answer 2.95
	#print(calc_toll(1, False, False)) #answer 1.9
	#print(calc_toll(3, False, True))  #answer 2.15
	#print(calc_toll(5, True, True))   #answer 1.05


	#Uncomment this when working on Problem 2
	
	
	if LCM(10,25) == 50:
		print("LCM(10,25) is correct")
	else:
		print(f"LCM(10,25) is incorrect.  You got {LCM(10,25)}, but the correct answer should be 50.")
	if LCM(90,342) == 1710:
		print("LCM(90,342) is correct")
	else:
		print(f"LCM(90,342) is incorrect. You got {LCM(90,342)}, but the correct answer should be 1710.")
	if LCM(45,240) == 720:
		print("LCM(45,240) is correct")
	else:
		print(f"LCM(45,240) is incorrect.  You got {LCM(45,240)}, but the correct answer should be 720.")
	'''


	 #Uncomment this when working on Problem 3

	for i in range(10):
		for j in range(i+1):
			print(int(combination(i,j)), end=' ')
		print()
	






