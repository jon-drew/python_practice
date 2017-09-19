max = 100
min = 0
correct = False
print ('Please think of a number between 0 and 100!')

while correct == False:
    currentGuess = (min+max)//2
    print ('Is your secret number ' + str(currentGuess) + '?')
    highLowInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if highLowInput == 'c':
        correct = True
        print ('Game over. Your secret number was: ' + str(currentGuess))
    elif highLowInput == 'h':
        max = currentGuess
    elif highLowInput == 'l':
        min = currentGuess
    else:
        print ("Sorry, I did not understand your input.")