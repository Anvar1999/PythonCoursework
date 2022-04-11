##Write code that prompts the user to enter a positive nonzero number and validates the input.


n = int(input("Enter a positive nonzero number: "))
if n>0:
    print(n,"is valid")
else:
    print(n, "is NOT valid")
