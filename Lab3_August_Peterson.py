print("Enter the amount of income you earned in 2023: ", end = "")
income = float(input())
print("Are you married or single?")
print("type m for married and s for single: ", end = "")
mStatus = input()
tax = float
bracket1 = .1
bracket2 = .12
bracket3 = .22
if mStatus == "m":
	if income >= 0 and income <= 22000:
		tax = income * bracket1
		print(f"You owe {tax} dollars")
	elif income > 22000 and income <= 89450:
		tax = (income - 22000) * (bracket2) + (22000 * bracket1)
		print(f"You owe {tax} dollars")
	elif income > 89450 and income <= 190750:
		tax = (income - 89450) * (bracket3) + (89450 - 22000) * (bracket2) + (22000 * bracket1)
		print(f"You owe {tax} dollars")
	else:
		print("You are either in debt, or your simply too rich")
else:
	if income >= 0 and income <= 11000:
		tax = income * bracket1
		print(f"You owe {tax} dollars")
	elif income > 11000 and income <= 44725:
		tax = (income - 11000) * (bracket2) + (11000 * bracket1)
		print(f"You owe {tax} dollars")
	elif income > 44725 and income <= 95375:
		tax = (income - 44725) * (bracket3) + (44725 - 11000) * (bracket2) + (11000 * bracket1)
		print(f"You owe {tax:.2f} dollars")
	else:
		print("You are either in debt, or your simply too rich")
		
