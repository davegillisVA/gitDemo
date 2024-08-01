import random

###############################################################
# FUNCTION to execute Game
def rps():
    player = "Dave"
    computer = "Computer"
    validChoices = ['rock', 'paper', 'scissors', 'quit']
    compChoices = ['rock', 'paper', 'scissors']
    playerChoice = 'zzz'
    playerW = 0
    computerW = 0
    ties = 0
###############################################################
# Create Welcome Banner
    welcome = """
    This is a simple game of luck!
    We call it Rock, Paper, Scissors
    You will be playing against your computer!
    BEST of LUCK!!!
    
    """
    print(welcome)
###############################################################
# Get Players Name
    player = input("And who do I have the pleasure of playing today? ")
    print(f"\nGood Luck {player}\n")

    while playerChoice not in validChoices:
        playerChoice = input(" Enter your Choice  (rock,paper,scissors)(quit to end game) ").lower()

###############################################################
# PLAY The Game
    while playerChoice != 'quit':

        computerChoice = random.choice(compChoices)
        print(f"     {computer} ", computerChoice, f"   {player} ", playerChoice)

        if playerChoice == 'rock' and computerChoice == 'scissors':
            print(" You Won!")
            playerW += 1
        elif playerChoice == 'scissors' and computerChoice == 'paper':
            print(" You Won! ")
            playerW += 1
        elif playerChoice == 'paper' and computerChoice == 'rock':
            print(" You Won! ")
            playerW += 1
        elif playerChoice == computerChoice:
            print(" Houston we have a problem.... IT's a Tie!")
            ties += 1
        else:
            print(" The Computer Wins Again!")
            computerW += 1
        playerChoice = 'zzz'
        while playerChoice not in validChoices:
            playerChoice = input(" Enter your Choice (rock,paper,scissors)(quit to end game) ").lower()
    return player, computer, playerW, computerW, ties

###############################################################
# FUNCTION to Print End of Game ScoreBoard
def scoreBoard(pName, cName, playerWins, computerWins, ties):

    print('\n{:>10}'.format(pName), "Won: ", '{:>6}'.format(playerWins))
    print('{:>10}'.format(cName), "Won: ",  '{:>6}'.format(computerWins))
    print(f"        There were {ties} ties")


###############################################################
# Main method to Launch Game
def main():

    pname, cname, pw, cw, t = rps()
    scoreBoard(pname, cname, pw, cw, t)

# Executes main method
main()


