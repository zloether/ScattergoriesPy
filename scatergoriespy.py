#!/usr/bin/env python
# https://github.com/zloether/ScattergoriesPy

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import random
import os
import playsound
import time
import sys



# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------
app_path = os.path.dirname(os.path.realpath(__file__))
categories_file_name = 'categories.md'
categories_file = os.path.join(app_path, categories_file_name)
buzzer = os.path.join(app_path, 'buzzer.mp3')
tick = os.path.join(app_path, 'tick.mp3')
alphabet = 'ABCDEFGHIJKLMNOPRSTW'

# defaults
num_rounds = 12
per_round = 12
timer = 3 * 60


# -----------------------------------------------------------------------------
# Scattergories game main function
# -----------------------------------------------------------------------------
def play(categories_file=categories_file, num_rounds=num_rounds, per_round=per_round, timer=timer):
    
    # get list of categories to use for this game
    categories_for_game = generate_categories_list(categories_file, num_rounds, per_round)

    letters_for_game = []
    for letter in alphabet:
        letters_for_game.append(letter)
    
    current_round = 1

    while current_round <= num_rounds:

        # clear the screen
        os.system('clear')

        # print the round we're in
        print('ROUND #' + str(current_round))

        # get a random letter for this round
        letter = letters_for_game.pop(random.randrange(0, len(letters_for_game)-1))

        # tell the players their letter for this round
        print('Letter: ' + str(letter))

        # lets play!
        play_round(categories_for_game)
        
        # lets players score the round before continuing
        input('Press ENTER to continue')
        
        # increment round counter
        current_round += 1
        



# -----------------------------------------------------------------------------
# Code to play a single round
# -----------------------------------------------------------------------------
def play_round(categories_list, per_round=per_round, timer=timer):
    
    # print list of categories
    i = 1
    while i <= per_round:
        print(str(i) + ') ' + categories_list.pop(0))
        i += 1

    # start timer
    run_timer(timer)

    # sound buzzer
    playsound.playsound(buzzer)


# -----------------------------------------------------------------------------
# Timer
# -----------------------------------------------------------------------------
def run_timer(timer=timer):
    time_left = timer
    sys.stdout.write('Seconds remaining ' + str(time_left))
    sys.stdout.flush()
    time_left -= 1
    time.sleep(1)

    while time_left > 0:

        if time_left <= 30 and time_left > 10:
            if time_left % 5 == 0:
                sys.stdout.write('...' + str(time_left))
                sys.stdout.flush()
                playsound.playsound(tick)
        
        elif time_left <= 10:
            sys.stdout.write('...' + str(time_left))
            sys.stdout.flush()
            playsound.playsound(tick)
        
        elif time_left % 30 == 0:
            sys.stdout.write('...' + str(time_left))
            sys.stdout.flush()
            playsound.playsound(tick)


        time_left -= 1
        time.sleep(1)

    print()



# -----------------------------------------------------------------------------
# Generate list of categories for this game
# -----------------------------------------------------------------------------
def generate_categories_list(categories_file=categories_file, num_rounds=num_rounds, per_round=per_round):
    # make sure we can find the categories file
    if not os.path.isfile(categories_file):
        print('ERROR: Cannot find categories files - ' + str(categories_file))
        exit()
    
    # initialize empty list of categories
    categories = []

    # open categories file and read each line into the categories list
    with open(categories_file, 'r') as f:
        contents = f.readlines() # read all the lines
        for line in contents:
            categories.append(line.strip())
    
    #print(len(categories))

    # initialize empty list to hold categories for this game
    categories_for_game = []
    while len(categories_for_game) < num_rounds * per_round:

        # get a random index from the list of all categories
        random_index = random.randrange(0, len(categories)-1)

        # read the category from the list of categories at that random index number
        # pop removes that element from the list after it is returned
        category = categories.pop(random_index)

        # store the category into the list of categories to use this game
        categories_for_game.append(category)

    
    #print(len(categories_for_game))
    #print(categories_for_game)

    return categories_for_game





# -----------------------------------------------------------------------------
# Run main
# -----------------------------------------------------------------------------
def __run_main():

    play()
    exit()






# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    __run_main()