"""
Write a program that gives simple math quizzes. The program should display two random numbers that are to be added, such as: 
247 + 129
The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. 
If the answer is incorrect, a message showing the correct answer should be displayed.
"""

### P #4

##import random
##
### main function
##def main():
##    # Local variables
##    num1 = 0
##    num2 = 0
##    correctAnswer = 0
##    userAnswer = 0
##
##    # Get numbers
##    num1 = random.randint(0, 999)
##    num2 = random.randint(0, 999)
##    
##    # Display math problem 
##    displayProblem(num1,num2)
##
##    # Get user answer
##    userAnswer = getAnswer()
##
##    # Calculate correct answer
##    correctAnswer = num1 + num2
##
##    # Display result
##    showResult(correctAnswer, userAnswer)
##
### The displayProblem function accepts the numbers
### and displays them
##def displayProblem(num1,num2):
##    print (format(num1, '5'))
##    print ('+', end='')
##    print (format(num2, '4'))
##    
### The getAnswer function gets and returns the user answer
##def getAnswer():
##    inputAnswer = int(input('Enter sum of numbers: '))
##    return inputAnswer
##    
### The showResult function tells if user answer is
### correct or not
##def showResult (correctAnswer, answer):
##    if correctAnswer == answer:
##        print ('Correct answer – Good Work!')
##    else:
##        print ('Incorrect... The correct answer is:', \
##               correctAnswer)
##
### Call the main function.
##main()

