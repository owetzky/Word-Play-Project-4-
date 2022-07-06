### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual): 


  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual):
      
      # if the letter is in the correct place in the secret word 
      if(letter == actual[index]):
        printColorfulLetter(letter, True, True)

      # if letter is not in the correct place
      else:
        printColorfulLetter(letter, True, False)

    else:
      printColorfulLetter(letter, False, False)
      
    print(Style.RESET_ALL + " ", end="")
  print()
### Main Program ###
    
# print ASCII art for game 

print(""" __      __                   __      ____    ___                         
/\ \  __/\ \                 /\ \    /\  _`\ /\_ \                        
\ \ \/\ \ \ \    ___   _ __  \_\ \   \ \ \L\ \//\ \      __     __  __    
 \ \ \ \ \ \ \  / __`\/\`'__\/'_` \   \ \ ,__/ \ \ \   /'__`\  /\ \/\ \   
  \ \ \_/ \_\ \/\ \L\ \ \ \//\ \L\ \   \ \ \/   \_\ \_/\ \L\.\_\ \ \_\ \  
   \ `\___x___/\ \____/\ \_\\ \___,_\   \ \_\   /\____\ \__/.\_\\/`____ \ 
    '\/__//__/  \/___/  \/_/ \/__,_ /    \/_/   \/____/\/__/\/_/ `/___/> \
                                                                    /\___/
                                                                    \/__/
     
""")

# print game name and rules
print("Welcome to Word Play!")
print()
print("=====================")
print("You have FIVE tries to get the word correct.")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length.")
print("If the letter is in the correct place, it will turn green.")
print("If the letter is in the word, buit NOT in the correct place, it will turn yellow.")
print("If the letter is NOT in the word, it will turn red.")
print()

# set the variable to default value 
sixLetterInput = ""

# set guess count <= 6
count = 0 

# define the parameters 


# set correct word
secretWord = "qwerty"

# set loop for user guess
while(sixLetterInput != secretWord and count != 6):
  sixLetterInput = input("Enter a six letter word: ")
  printGuessAccuracy(sixLetterInput, secretWord)
  count += 1
  if(sixLetterInput == secretWord):
    print()
    print(f"You win! Great job, it took you {count} guesses!")

  #if attempts == 6 game ends user must start over
  if(sixLetterInput != secretWord and count == 6):
      print()
      print(f"You lost! You guessed {count} times. Play again?")

# if answer is correct or wrong land here
if(count == 6):
  printGuessAccuracy(sixLetterInput, secretWord)

print()
