#evenodd.py
n=int(input("enter a number:"))
if(n==0):
	print("n:is invalid input,enter +ve value only:");
elif(n<0):
	print("n:is invalid input,enter +ve value only:");
elif(n%2==0):
	print(n,"is EVEN")
elif(n%2!=0):
	print(n,"is odd")