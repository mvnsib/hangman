#task 2 step 1
#task 2 step 2
import random

#task 1 step 1 
fruits = ["Apple", "Banana", "Pineapple", "Mango", "Peach"]

#task 3 step 1 & 2
guess = input("Input a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# task 1 step 2
word_list = fruits

#task 2 step 3
word = random.choice(word_list)


#task 1 step 3
print(word)
