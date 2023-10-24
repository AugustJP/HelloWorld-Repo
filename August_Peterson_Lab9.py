groceryList = []
costOfItem = []
#item = input("Enter your groceryList item: ")
#cost = input("Enter your groceryListItem Cost in Dollars: ")
while True:
	item = input("Enter your groceryList item: ")
	if item == "DONE":
		break
	cost = int(input("Enter your groceryListItem Cost in Dollars: "))
	groceryList.append(item)
	costOfItem.append(cost)
print(f"My grocery list is {groceryList}")
print(f"Cost for each item {costOfItem}")

groceryDict = {}
for i in range(len(groceryList)):
	groceryDict[groceryList[i]] = costOfItem[i]

print(groceryDict)

totalCost = sum(costOfItem)
print(f"Total amount spent on grocery shopping is {totalCost}")

groceryDict2 = {"Butter": 7, "Milk": 5, "Apples": 8}

def grocery_purchases(purchase1, purchase2):
	if len(purchase1) != len(purchase2):
		return False
	
	for item, cost in purchase1.items():
		if item not in purchase2 or purchase2[item] != cost:
			return False
	
	return True

if grocery_purchases(groceryDict, groceryDict2):
    print(f"{groceryDict} is the same as {groceryDict2}")
else:
    print(f"{groceryDict} is NOT the same as {groceryDict2}")

def compare_purchases(purchase1, purchase2):
	for item, cost in purchase1.items():
		if item in purchase2:
			if cost < purchase2[item]:
				print(f"{item} is cheaper in purchase1.")
			elif cost > purchase2[item]:
				print(f"{item} is cheaper in purchase2.")
		else:
			print(f"{item} is only on purchase1.")
    
	for item in purchase2:
		if item not in purchase1:
			print(f"{item} is only on purchase2.")

compare_purchases(groceryDict, groceryDict2)

groceryPurchase = { 
	"Mayo": {"price": 5, "QTY": 3}, 
	"HotDog": {"price": 90, "QTY": 1}, 
	"Applesauce": {"price": 2, "QTY": 10}
}
	
for item, blart in groceryPurchase.items():
	QTY = blart["QTY"]
	price = blart["price"]
	if QTY == 1:
		print(f"Purchase {QTY} {item} at cost ${price} each.")
	else:
		print(f"Purchase {QTY} {item}s at cost ${price} each.")
	
	
	
	
	
