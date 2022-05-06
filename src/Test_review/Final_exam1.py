#part 1 

def main():

   mystr = input("Enter your String:")
   mystr.lower()
   #index = 0, index is useless here
   vowelSet = set(['a','e','i','o','u'])
   #vowels = 0, vowels is useless here
   #consonants = 0, consonants is useless here

   #Either pass vowelSet as argument or define them explicitly in the methods
   runVowels(mystr, vowelSet)
   runConsonants(mystr, vowelSet)

def runVowels(mystr, vowelSet):
    #index, vowels needs to be defined and assigned a default value here
    index = 0
    vowels = 0

    while index < len(mystr):
        if mystr[index] in vowelSet:
            vowels += 1

        # You need to increment index outside of the condition
        index += 1
    print('This string consists of ', vowels , 'vowels')

def runConsonants(mystr, vowelSet):
    #index, consonants needs to be defined and assigned a default value here
    index = 0
    consonants = 0
    while index < len(mystr):
        if mystr[index] not in vowelSet:
            consonants += 1

        # You need to increment index outside of the condition
        index += 1
    print('This consists ', consonants, 'consonants')

main()

