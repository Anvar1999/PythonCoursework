first_name = input("Hello, What's your first name? ")
last_name  = input("Ok, What's your last name? ")
print("What do you call a bear with no teeth\nA gummy bear!")
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
total = num1 + num2 
print("Total", total)
num3 = int(input("Enter num3"))
num4 = int(input("Enter num4"))
num5 = int(input("Enter num5"))
answer = (num3 + num4) * num5
print("answer", answer)
start_slices = int(input("How many slices of pizza you started with? "))
eaten_slices = int(input("How many slices of pizza have you eaten? "))
calc_slices = start_slices - eaten_slices 
print("Left slices", calc_slices)
user = input("What's your name? ")
user_age = int(input("How old are you? "))
plus1 = user_age + 1 
print(user,"next birthday you will be ",plus1)
total_bill = int(input("What's total price of the bill? "))
diners = int(input("How many diners? "))
split_bill = total_bill/diners
print("Each person must pay", split_bill)
number_days = int(input("Tell me numbers of days"))
calc_hours = number_days * 24 
calc_minutes = calc_hours * 60 
calc_seconds = calc_minutes * 60
print("Number of days", number_days,"\nHours in those days",calc_hours,"\nminutes in those days",calc_minutes)
print("seconds in those days", calc_seconds)
converter = int(input("How many kgs you want to convert to pounds? "))
calc_converter = 2.204 * converter 
print(converter, "kgs in pounds will be ", calc_converter)
task = int(input("enter number over hundred"))
task2 = int(input("enter number under ten"))
calc_task = task//task2
print(task,"is",calc_task,"times more than", task2)
