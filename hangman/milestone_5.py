import random


class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list      # List of words
        self.num_lives = 5      # Number of lives given to the user
        self.word = random.choice(self.word_list).lower()       # Randomly chooses the word from the list
        self.word_guessed = ["_" for _ in self.word]        # Replaces the letters in the word with _
        self.num_letters = len((self.word))     # Number of letters
        self.list_of_guesses = []       # Tracks the letters that has been guessed

    def check_guess(self, guess):
        guess = guess.lower()   
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):      # for loop to go through the word and index it
                if self.word_guessed[i] == "_" and guess == letter:     # Checks if the position of the letter contains an _ and whether the guess == letter
                    self.word_guessed[i] = letter       # Replaces the _ with the letter that has been guessed

                    self.num_letters -= 1       # Deducts 1 point for the letter to track whether the user has guessed all the letters
                    #print(self.num_letters)

            print("".join(self.word_guessed))       

        else:       # If the user guesses the wrong letter it will deduct 1 point from their LP
            self.num_lives -= 1
            print(
                f"Sorry, {guess} is not in the word. \n You have {self.num_lives} lives left."
            )

    def ask_for_input(self):
        guess = input("Input a letter: ")       # Prompts the user to input a letter

        if len(guess) != 1 and not guess.isalpha():     # Checks if the letter is an alphabet and a single character
            print("Invalid letter. Please, enter a single alphabetical character.")

        elif guess in self.list_of_guesses:     # If the letter has been guessed
            print("You already tried that letter!")
        else:       # If all conditions are fine
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):       # Function to play the game
    num_lives = 5
    game = Hangman(word_list, num_lives)        # Instance of the Hangman class where we pass in the arguements
    while True:     # While loop to keep the game ongoing until a condition has been met
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters != 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break



word_list = ["Apple", "Banana", "Pear"]
play_game(word_list)
