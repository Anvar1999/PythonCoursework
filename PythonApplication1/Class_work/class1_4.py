MIN_SALARY = 30000
MIN_YEARS = 2
salary = int(input('What is your salary? '))
years_on_job = int(input('How many years on this job? '))

if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for the loan. ')
else:
    print("You don't qualify for this loan. ")
