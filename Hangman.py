#This is hangman! Yeah!
#Is hanging somebody executive function?

print("Welcome to hangman!")
print("")
print("Below you will find a series of dots in a string. That is the length of the word you have to guess. It will update itself as you guess correctly.")


SecretWord = "Banaan"
FaultAmount = 0
FaultAllowance = 11
CurrentGuess = ""
CurrentGuessList = []


#Loop to make a list for computing new guesses, and a string to display for the guesser
for character in SecretWord:
    CurrentGuess = CurrentGuess + "."
    CurrentGuessList.append(".")


print("")
print(CurrentGuess)
print("")
print("A valid guess would be a single letter, or the entire word you have to guess if you are feeling confident.")
print("Please note that if you type a three letter guess that is not the entire word, the program will consider it a wrong guess, regardless of its content")
print("")


#This function checks how many wrong guesses have been made, then determines which print statement to display, or if you've been 'hanged'
#Niels wilt weten waarom de case FaultAmount == FaultAllowance per sé zo moet en niet 'case FaultAllowance:' kan zijn 
def Faultulator(FaultAmount):
    match(FaultAmount):
        case FaultAmount if FaultAmount == FaultAllowance:
            print("")
            print("You have been hanged!")
            print("")
            exit()
        case 1:
            print(f"Wrong! You have made {FaultAmount} wrong guess. You have {FaultAllowance - FaultAmount} tries left.")
            print("")
            return
        case FaultAmount if FaultAmount > 1:
            if FaultAllowance - FaultAmount > 1:
                print(f"Wrong! You have made {FaultAmount} wrong guesses. You have {FaultAllowance - FaultAmount} tries left.")
                print("")
                return
            if FaultAllowance - FaultAmount == 1:
                print(f"Wrong! You have made {FaultAmount} wrong guesses. You have {FaultAllowance - FaultAmount} try left.")
                print("")
                return
        case _:
            print(f"FaultAmount({FaultAmount}) has a value other than an integer 1 or greater, or is greater than the allowed amount of faults. This is a bug.")
            print("")
            exit()


#This function updates the CurrentGuess and CurrentGuessList variable with correct guesses and puts them on the correct position.
#This function also checks if you have guessed the word by inputting all the correct letters one by one. 
def HangManCompute(Letter):
    Indexer = 0
    while SecretWord.find(Letter, Indexer) > -1:
        Indexer = SecretWord.find(Letter, Indexer)
        CurrentGuessList[Indexer] = Letter
        Indexer += 1
        continue
    CurrentGuess = "".join(CurrentGuessList)
    if CurrentGuess == SecretWord:
        print("")
        print("You guessed it! You are also not dead!")
        print("")
        exit()
    print("")
    print(f"Correct! You currently know the following: {CurrentGuess}. Way to go! Don't die now!")
    print("")
    return

#This function increases the tally of faults if one has been made. It also checks if you guessed the word by typing it in entirely.
#If you guess a correct singular letter, it calls for the compute function.
def Guess(Letter, FaultAmount):
    match Letter:
        case Letter if Letter == SecretWord:
            print("You guessed it! You are also not dead!")
            print("")
            exit()
        case Letter if len(Letter) > 1:
            FaultAmount += 1
            Faultulator(FaultAmount)
            return FaultAmount
        case Letter if Letter in SecretWord:
            HangManCompute(Letter)
            return
        case Letter if Letter not in SecretWord:
            FaultAmount += 1
            Faultulator(FaultAmount)
            return FaultAmount


while CurrentGuess.find(".") != -1:
    print("Please make a guess:")
    Letter = input()
    FaultAmount = Guess(Letter, FaultAmount)
