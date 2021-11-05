mail = input("please input your mail adress")
a = "@" and "." in mail
if a==True:
	print("it is a real mail adress")
else:
	print("it is not a real mail adress")