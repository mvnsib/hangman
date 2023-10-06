import random
import milestone_2

fruits = ["Apple", "Banana", "Pineapple", "Mango", "Peach"]


word_list = fruits

word = random.choice(word_list)
print(word)

guess = input("Guess the letter: ").lower()


def check_guess(guess):
    if guess.upper() in word or guess.lower() in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    check_guess(guess)
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


ask_for_input()
