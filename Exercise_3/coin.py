# File:         coin.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Description:  Coin object and tossing

import random

# Class definition

class Coin:
    def __init__(self, sideup, material, currency):
        

        self.__material = material
        self.__currency = currency


    def toss_the_coin(self):
        
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # Accessor method ("getter")
    def get_sideup(self):
        return self.__sideup

    # Mutator method ("setting")
    def set_material(self, material):
        self.__material = material

    # Accessor method ("getter")
    def get_material(self):
        return self.__material

    def set_currency(self):

        if random.randint(0,4) == 0:
            self.__currency = 'Euro'
        elif random.randint(0,4) == 1:
            self.__currency = 'Pounds'
        elif random.randint(0,4) == 2:
            self.__currency = 'Reais'
        elif random.randint(0,4) == 3:
            self.__currency = 'Dollar'
        else:
            self.__currency = 'Yen'
        
    def get_currency(self):
        return self.__currency




    
