''' 
August Peterson, #121, sec 05
8/31/23
Calculating the age of animals in a year, month, day format
'''
import math
print ("Enter your age:  ")
age = float(input())
dog_age = age * 722
age_dog_years = dog_age // 1
age_dog_months = ((dog_age % 1) * (12) // 1)
age_dog_days = ((dog_age % 1) * 12 % 1 * 30 // 1)

cat_age = age / 9
age_cat_years = cat_age // 1
age_cat_months = ((cat_age % 1) * (12) // 1)
age_cat_days = ((cat_age % 1) * 12 % 1 * 30 // 1)

horse_age = 3 * (((math.pow(age, 2) -47) / 7) + 12)
age_horse_years = horse_age // 1
age_horse_months = ((horse_age % 1) * (12) // 1)
age_horse_days = ((horse_age % 1) * 12 % 1 * 30 // 1)


print (f"Your age in dog years is {age_dog_years} years {age_dog_months} months {age_dog_days} days")
print (f"Your age in cat years is {age_cat_years} years {age_cat_months} months {age_cat_days} days")
print (f"Your age in horse years is {age_horse_years} years {age_horse_months} months {age_horse_days} days")



