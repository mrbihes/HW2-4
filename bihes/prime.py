x = int(input("please put a number : "))
stat = True
if x>1 :
	for i in range(2,x):
		if x%i == 0 :
			stat = False
			break
	if stat == True :
		print ("it is prime")
	else :
		print ("it is no prime")
elif x == 2 :
	print ("it is prime")
else :
	print ("it is  not prime")
