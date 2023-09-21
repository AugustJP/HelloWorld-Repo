'''
August Peterson
Lab 5
Multiplication Table, Finding Prime Numbers less than 250, finding the same thing but the unit digit is 3, and finding a prime number or a perfect number
'''
for i in range(1,9):
	print()
	for j in range(1,11):
		q = i * j
		print(f"{q:2}",end=" ")

boolean = True
for i in range(1,250):
	for j in range(2,i):
		if i % j == 0:
			boolean = False
	if boolean:
		print(i)
	boolean = True

for i in range(1,250):
	if i > 1 and i % 10 == 3:
		for j in range(2,i):
			if i % j == 0:
				break
		else:
			print(i)

boolean = True
for i in range(1,250):
	countD = 1
	if i > 1:
		for j in range(2,i):
			if i % j == 0:
				boolean = False
				countD += j
		if countD == i:
			print(i)
		elif boolean:
			print(i)
	boolean = True
