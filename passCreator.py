import random
import string

letters = string.ascii_letters
letterGuess = ""
theNumOfLetters = int(input("how many letters do you want in your password? "))
for i in range(theNumOfLetters):
    letterGuess += random.choice(letters)


numsGuess = ""
digits = string.digits
theNumOfDigits = int(input("how many digits do you want in your password? "))
for i in range(theNumOfDigits):
    numsGuess += random.choice(digits)

theSuggestPass = letterGuess + numsGuess
print(f"the suggested password is: {theSuggestPass} .")