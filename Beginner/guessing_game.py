# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

from random import randint
# picking random number
rand_num = randint(1,100)

guesses = 0
user_input = 0
privous_guess=0

while True: 
    privous_guess = user_input
    user_input = int(input('Guess a number between 1 and 100: '))
    
    if user_input == rand_num:
        print(f'Yay! You have got the number in {guesses} guesses.')
        break
    elif user_input<1 or user_input>100: 
        print('Input OUT OF BOUND!')
        continue
    diff = abs(user_input - rand_num)
    
    # Checking first time guess
    if guesses ==0:
        if diff <=0 and guesses == 0:
            print('WARM!')
        else:
            print('COLD!')
    elif abs(privous_guess-rand_num) > abs(user_input - rand_num):
        print('WARMER')
    else:
        print('COLDER')
       
    guesses+=1
    
