numOfWords = 0
numOfLetters = 0
numOfDigits = 0
# taking input from user
text = input("Enter a text of numbers : ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
         numOfLetters = numOfLetters + 1

    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1

    elif x == ' ':
        numOfWords = numOfWords + 1
#finding how many words, digits and letter user put
print ('num of Words :', numOfWords)
print ('num of Digits :', numOfDigits)
print ('num of Letters :', numOfLetters)
