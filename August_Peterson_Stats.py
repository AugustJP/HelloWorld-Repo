def meanFinder(data):
	mean = 0
	count = 0
	total = 0
	for i in data:
		total += i
		count += 1
	mean = total / count
	return mean
	
	
	
def medianFinder(data):
	median = 0
	data.sort()
	count = 0
	for i in data:
		count += 1
	if count % 2 == 0:
		x = data[((count // 2))]
		y = data[((count // 2) - 1)]
		return mean([x, y])
	else:
		return data[count // 2]
	
	


