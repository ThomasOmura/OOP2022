import roll

# Main function definition

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