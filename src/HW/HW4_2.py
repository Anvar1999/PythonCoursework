#Write a program that lets the user enter a nonnegative integer and validates it, 
#then uses a loop to calculate the factorial of that number. 


#take the nonnegative integer from the user
n = int(input("Input the nonegative integer: "))
def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
print(fact(n)) #n is the sample value it will returns, let's say n is equal to 7:  7!==> 7*6*5*4*3*2*1 =5040

