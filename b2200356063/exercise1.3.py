import random
number = random.randint(0,101)
a = int(input("please input a number"))
while a != number:
	while a > number:
		print("higher!")
		a = int(input("please input a lower number"))
	while a < number:
		print("lower!")
		a = int(input("please input a higher number"))
print("well done:)")



