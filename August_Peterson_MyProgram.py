from August_Peterson_Stats import meanFinder
from August_Peterson_Stats import medianFinder

#with open("500DayFruitData.txt", "r") as data:
#calc = open("August_Peterson_MyProgram.py" , "r")
data = open("500DayFruitData.txt", "r")

output = open("August_Peterson_Output.txt" , "w")

apple_list = []
banana_list = []
strawberry_list = []
total_list = []


for line in data:
	line = line.split()
	if line[0] != "Day":
		total_list.append(int(line[2]))
	if line[1] == "apple":
		apple_list.append(int(line[2]))
	elif line[1] == "banana":
		banana_list.append(int(line[2]))
	elif line[1] == "strawberry":
		strawberry_list.append(int(line[2]))
			
apple_mean = meanFinder(apple_list)
apple_median = medianFinder(apple_list)

banana_mean = meanFinder(banana_list)
banana_median = medianFinder(banana_list)

strawberry_mean = meanFinder(strawberry_list)
strawberry_median = medianFinder(strawberry_list)

total_mean = meanFinder(total_list)
total_median = medianFinder(total_list)

output.write(f"The mean number of apples eaten is {apple_mean:.2f}\n")
output.write(f"The median number of apples eaten is {apple_median:.2f}\n")
output.write(f"The mean number of bananas eaten is {banana_mean:.2f}\n")
output.write(f"The median number of bananas eaten is {banana_median:.2f}\n")
output.write(f"The mean number of strawberries eaten is {strawberry_mean:.2f}\n")
output.write(f"The median number of strawberries eaten is {strawberry_median:.2f}\n")
output.write(f"The mean number of all fruits eaten is {total_mean:.2f}\n")
output.write(f"The median number of all fruits eaten is {total_median:.2f}\n")
