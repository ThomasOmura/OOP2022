# File: demo_coin.py
# Description: Coin object and tossing

import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:

    # The __init__ method initiallizes the
    # sideup data attribute with 'Heads'

    def __init__(self):
        self.sideup = 'Heads'
    
    # The toss method generates a random number
    # in a range of 0 through 1. if the number
    # is 0, then side up is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
             self.sideup = 'Heads'
        else:
             self.sideup = 'Tails'

    # The get_sideup method returns the vale
    # references by sideup.

    def get_sideup(self):
        return self.sideup
    
    # The main function.
    def main():

        # Create an object from the Coin class.
        my_coin = Coin()

        #  Display the side of the coin that is facing up 
        print('This side up', my_coin.get_sideup())

        # Toss the coin
        my_coin.toss()

         #  Display the side of the coin that is facing up 
        print('This side up', my_coin.get_sideup())

    # Call the main function
    main()




