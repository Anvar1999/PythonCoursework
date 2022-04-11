"""
even_numbers = [2, 4, 6, 8, 10]

print(even_numbers)
"""
"""
even_numbers = list(range(10))

print(even_numbers)
"""

"""
letters = ['a', 'b', 'c', 'd']
letters2 = letters * 4
print(letters)
print(letters2)
"""
"""
letters = ['a','b','c','d']
for x in letters:
    print(x)
    """
"""
numbers = list(range(1, 10, 2))
total = 0 

for x in numbers:
    print(x)
    total = total + x

print(total)
"""
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#[0] in the list prints first number, [1] prints the second number, for last element use n-1
print(numbers[0]) #  1
# if you use negative numbers it goes backwards 
print(numbers[-1])# 8

# you cannot use beyong values for index, otherwise you will recieve error
"""

"""
numbers = [1,2,3,4,5]
index = 0

while index < 5:
    print(numbers[index])
    index += 1
    """
    
numbers = list(range(1, 98374656, 6))
index = 0
# len used for not go beyond given numbers 
while index<len(numbers):
    print(numbers[index])
    index += 1
