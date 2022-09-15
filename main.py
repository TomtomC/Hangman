import display as dis
import stages as stag
import words as wrd
import txtcolor as colr

import os ## for clearing the terminal screen to allow hangman and letter changes without clogging up the terminal


## Hangman game
def main():

    lives = 6  # DO NOT CHANGE. This value is needed to determine the hangman stages.

    ########## word actions
    chosen_word = wrd.the_word() # find the word

    chosen_word = chosen_word.lower() # a precaution in case any of the manually added words contains captial letters.

    display = dis.display__(chosen_word) ## create display and correct number of _ spaces

    #print(chosen_word) # for debugging

    word_length = len(chosen_word) # for the loop below
    ##########

    ########## game actions
    end_of_game = False
    while not end_of_game:
        
        guess = input("Enter a letter to guess the word: \n").lower()

        for n in range(word_length):
            letter = chosen_word[n]
            if letter == guess:
                display[n] = guess
            
        
        if guess not in chosen_word:
                lives -= 1 ##lose a life
        
        os.system('cls') ### clear terminal screen


        if "_" not in display:
            colr.txtGreen(stag.stage(lives)) ### print hangman symbol
            colr.txtGreen(display) ## print guesses and spaces
            colr.txtGreen(f"You correctly guessed: {chosen_word}!")
            end_of_game = True
            colr.txtGreen("You win!")

        elif lives == 0:
            colr.txtRed(stag.stage(lives)) ### print hangman symbol
            colr.txtRed(display) ## print guesses and spaces
            end_of_game = True
            colr.txtRed(f"TThe correct word was: {chosen_word}")
            colr.txtRed("You lose!")

        else:
            print(stag.stage(lives)) ### print hangman symbol
            print(display) ## print guesses and spaces


## this is where the game starts.
if __name__ == "__main__":
    main()  
