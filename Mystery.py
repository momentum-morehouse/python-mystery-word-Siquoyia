# computer ask user to guess
import random
file_object = open('words.txt', 'r')
words_list = file_object.readlines()
#print("random item from list is: ", random.choice(words_list))
def computer_guess():
    new_word = random.choice(words_list)
    print(new_word)
    return new_word

def say_hello(word):
    if len(word) > 4:
        print('hello', word)
    else:
        print('not valid')
say_hello(computer_guess())
 
    
def guess():
    guess = input("Enter Guess Here")
    return guess
# confirm correct or incorrect answer
def validate(guess, word):
    if guess in word:
        print("yes")
    #If the user guesses the same letter twice       
#def guess(same_letter, word):
    #if guess same_letter twice in word:
        #print("You already guessed that letter, try again: ")
        # 
computer_guess()       