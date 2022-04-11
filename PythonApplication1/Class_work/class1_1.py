"""
hours = int(input('Enter the hours worked this week: '))

while hours <= 0 or hours > 60:
    
    hours = int(input('Number of hours is not correct. Enter the correct number of hours worked this week: '))

pay_rate = float(input("Enter the hourly pay rate: "))
while pay_rate < 16 or pay_rate > 60:
    pay_rate = float(input('Enter the hourly pay rate: '))

gross_pay = hours * pay_rate

print('Gross pay: $', format(gross_pay, ',.2f'))
"""

"""
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours,':',minutes,':', seconds)
"""
"""
## use end = '' to not jump to next line
for r in range(4):
    for c in range(7):
        print('*', end = '')
    print('')
"""
"""
for r in range(5):
    for c in range(r+1):
        print('*', end = '')
    print('')
    """

total = 0
for count in range(1,4):
  total += count
print(total)