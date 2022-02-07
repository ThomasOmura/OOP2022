
from random import Random, randint


import random
from turtle import color

#Class Definition

class Dice:
    def __init__(self, roll, color, brand):

        self.__roll = roll 
        self.__color = color
        self.__brand = brand
    
    def roll_the_dice(self):
        if random.randint(1, 6) == 1:
            self.__roll = '1'
            
        elif random.randint(1, 6) == 2:
            self.__roll = '2'
        elif random.randint(1, 6) == 3:
            self.__roll = '3'
        elif random.randint(1, 6) == 4:
            self.__roll = '4'
        elif random.randint(1,6) == 5:
            self.__roll = '5'
        else:
            self.__roll = '6'

    # Accessor method ("getter")
    def get__rolls(self):
        return self.__roll 

    # Mutator method ("setting")  
    def set__color(self):
        self._color = color

    # Accessor method ("getter")
    def get__color(self):
        return self.__color


    def brand(self):
        if random.randint(1, 3) == 1:
            self.__brand = 'Lindorm'
        
        elif random.randint(1, 3) == 2:
            self.__brand = 'Level up'
        else:
            self.__brand = 'Harps Corp'
    
    def get_brand(self):
        return self.__brand
    

import roll

def main():

    the_roll = roll.Dice( 1, "Red", "Lindorm")

    print("Rolling the dice...")
    the_roll.roll_the_dice()
    print("The number is:", the_roll.get__rolls())

    print("The color of the dice is ...", the_roll.get__color())
    
    the_roll.brand()
    print("The brand of the dice is...", the_roll.get_brand())
    

# Calling the main function
main()