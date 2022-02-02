# File:         main.py
# Author:       Sanna Maatta
# Description:  Main function for coin 

from locale import currency
import coin

# Main function definition

def main():

    my_coin = coin.Coin("Tails", "Silver", "Dollar")

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

    print("Material is...", my_coin.get_material())

    my_coin.set_material("Gold")
    print("Material is now:", my_coin.get_material())

    print("The currency is...", my_coin.get_currency())
    my_coin.set_currency()
    print("The new currency is...", my_coin.get_currency())

    

# Calling the main function
main()
