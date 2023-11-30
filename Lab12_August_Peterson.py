
nums = open("randomValues.txt", "r")
	
numList1 = []
numList2 = []
	
for i in nums:
	i = i.strip()
	numList1.append(i)
	
thumbsUp = True
for i in numList1:
	try:
		n = int(i)
		numList2.append(n)
	except ValueError:
		thumbsUp = False

def mins(n):	
	if len(n) == 1:
		return n[0]
	temp_min = mins(n[1:])
	if n[0] < temp_min:
		return n[0]
	else:
		return temp_min
	
def maxs(n):	
	if len(n) == 1:
		return n[0]
	temp_max = maxs(n[1:])
	if n[0] > temp_max:
		return n[0]
	else:
		return temp_max
	
	
	
	
	
def extrema(nums, mn = True, mx = True):
	if mn == True and mx == True:
		return(f"the min is {mins(nums)} and the max is {maxs(nums)}")
	if not mx and mn:
		return (f"the min is {mins(nums)}")
	if not mn and mx:
		return (f"the max is {maxs(nums)}")
	
	
print(extrema(numList2))
	
nums.close()	
	
	
	
	
	
		
