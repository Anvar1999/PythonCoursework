#Main function
def main():
  #Declare Variables
  counter = 0
  increaseYear = 0
  maxYear = 0
  maxYearPosition = 0
  minYear = 0
  minYearPosition = 0
  averagePeriod = 0

  #Initialize "lists"
  listNumbers = []
  listNumberAverage =[]
  #Generate a list with numbers from 1950 to 1991
  listYears = [i for i in range(1950,1991)]

  #Try and Except
  try:
    #Open File
    fileRead = open("USPopulation.txt", "r")

    #Count the number of lines with values
    for i in fileRead:
      counter = counter + 1

    #Set the listNumbers size
    for j in range(counter):
      listNumbers.append(0)

    #Go back to the beggining of the file
    fileRead.seek(0)
    
    #Using a for loop read each line and fill listNumbers
    for k in range(counter):
      listNumbers[k] = int(fileRead.readline())
      #Use the first number as a guide later on
      minYear = listNumbers[0]

    #Loop to calculate the average and find min and max
    for l in range(0,counter,+1):
      
      #Stop loop if there's not more years to calculate average
      if (l+1) == counter:
        break
      
      #Calculate average on the year
      increaseYear = (listNumbers[l+1] - listNumbers[l])/2
      
      #Each time it found a greatest increase population between years set that number on maxYear plus save the index location
      if increaseYear > maxYear:
        maxYear = increaseYear
        maxYearPosition = l+1

      #Each time it found a smallest increase population between years set that number on minYear plus save the index location
      if minYear > increaseYear:
        minYear = increaseYear
        minYearPosition = l+1
    
    #Calcualete the average during the period
    averagePeriod = (listNumbers[counter-1] - listNumbers[0])/(counter-1)

    #Print the annual change of population in the period
    print("The average annual change in population during the time period is", '{0:,.2f}'.format(averagePeriod, ".2f"))
    #Print the greatest increase in population year
    print("The year with the greatest increase in population was", listYears[maxYearPosition])
    #Print the smallest increase in population year
    print("The year with the smallest increase in population was", listYears[minYearPosition])

    fileRead.close()

  #Handdle File not Found Error
  except FileNotFoundError:
    print("File does not exist")

  #Handdle IndexError
  except IndexError as error:
    print("Index Invalid")

  #Handdle any other error
  except Exception as exception:
    print("Something goes wrong!")

#Call main function
main()  