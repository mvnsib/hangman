import random
import milestone_2
import milestone_3


class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in self.word:
                if self.word[i].lower() == guess:
                    self.word_guessed[i] == self.word[i]

            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(
                f"Sorry, {guess} is not in the word. \n You have {self.num_lives} lives left."
            )
            # print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Input a letter: ").lower()
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
