"""
following formula: 
calories from fat = fat grams × 9
Next, she calculates the number of calories that result from the
carbohydrates, using the following formula:
calories from carbs = carb grams × 4
"""


def main():
    fat_gramms = int(input('Please enter the fat gramms: '))
 ## prompting user to enter values of fat_gramms 
    fat_calculation(fat_gramms)

    carbohydrate_gramms = int(input('Please enter the carbohydrate gramms: '))
## prompting user to enter values of carbohydrate_gramms
    carbohydrate_calculation(carbohydrate_gramms)

## function that calculated the user input, and returns the answer with calory 
def fat_calculation(fat_gramms):
    
    calories_from_fat = (fat_gramms * 9)
    print('This is the calory of Fat you entered', calories_from_fat)

## function that calculated the user input, and returns the answer with calory
def carbohydrate_calculation(carbohydrate_gramms):

    calories_from_carbs = (carbohydrate_gramms * 4)
    print('This is the calory of carbohydrate you entered', calories_from_carbs)

main()