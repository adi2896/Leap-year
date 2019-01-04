file=open("input.txt","r")
try:
	for y in file.readlines():
		if((int(y)%400==0) or ((int(y)%4 ==0) and (int(y)%100 !=0))):
			print(y.rstrip()),
			print("is a leap year")
		else:
			print(y.rstrip()),
			print("is not a leap year")

except ValueError:
    pass  # do nothing!
file.close()
