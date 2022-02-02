import random

class Dice:

    #Initializes the attributes
    def __init__(self, sideup):
        self.sideup = sideup
        

    #tosses the dice randomly and assigns the random value to a number
    def roll(self):
        if random.randint(0,5) == 0:
            self.sideup = '1'
        elif random.randint(0,5) == 1:
            self.sideup = '2'
        elif random.randint(0,5) == 2:
            self.sideup = '3'
        elif random.randint(0,5) == 3:
            self.sideup = '4'
        elif random.randint(0,5) == 4:
            self.sideup = '5'
        else:
            self.sideup = '6'
        
    #Gets the rolled dice
    def get_sideup(self):
        return self.sideup



def main():
    
    print("Rolling the dice...")
    
    first_dice =  Dice('3')
    second_dice = Dice('2')


    #Rolls the first dice and gets random number
    first_dice.roll()
    #changes the str into an integer
    first_dice = int(first_dice.get_sideup())
    print("First dice:", first_dice)

    second_dice.roll()
    second_dice = int(second_dice.get_sideup())
    print("Second dice:", second_dice)
    #sums the two dices
    sum_dice = first_dice + second_dice

    print("Sum of dice:", sum_dice)


main()