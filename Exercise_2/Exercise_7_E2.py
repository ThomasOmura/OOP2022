import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'


    def toss_the_coin(self):
        
        if random.randint(0,4) == 0:
            self.sideup = 'Heads'
        elif random.randint(0,4) == 1:
            self.sideup = 'Fell into rabbithole'
        elif random.randint(0,4) == 2:
            self.sideup = 'Lost in space'
        elif random.randint(0,4) == 3:
            self.sideup = 'Is upright on the ground'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

# Main function definition

def main():

    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())


# Calling the main function
main()