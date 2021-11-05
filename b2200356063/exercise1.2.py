def is_it_email():
	a = "@" and "." in mail
	if a==True:
		return True
	else:
		return False
mail = input("please input your mail adress")
print(is_it_email())
