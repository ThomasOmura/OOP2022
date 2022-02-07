import random

def main():
    player1 = 0
    player2 = 0
    player3 = 0
    rounds = 1
    
    while rounds != 2:

        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        player3 = dice_roll()

        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))
        print("Player 3 Roll: " + str(player3))

        if player1 < player2 and player3:

            print("Player 1 is out of the game!")
        
        elif player2 < player1 and player3:
            print("Player2 is out of the game!")
            
        else:
            print("Player 3 is out of the game")

        rounds = rounds + 1

   
def dice_roll():
        diceRoll = random.randint(1, 6)
        return diceRoll
        
        
main()