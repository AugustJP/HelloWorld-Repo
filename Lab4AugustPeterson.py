'''
August Peterson
Lab4
Find proper divisor, perfect number, abundant number, deficient number
'''
num = int(input())
df = 0
countP = 0
ab = 0
perf = 0
print("Enter an upper bound for a check:",num)
print(f"Between 1 and {num} there are")
for i in range(1, num+1):
	countPD = 0
	for j in range(1, i):
		if i % j == 0:
			countPD += j
			
	if countPD == i:
		perf += 1
	elif countPD < i:
		ab += 1
	elif countPD > i:
		df += 1
			
print(ab, "deficient numbers")
print(perf, "perfect numbers")
print(df, "abundant numbers")



