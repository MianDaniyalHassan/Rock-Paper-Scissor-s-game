import random
'''
1 for Rock
-1 for Paper
0 for Scissors
'''

computer = random.choice([1, -1, 0])
youstr = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
youDict = {'r': 1, 'p': -1, 's': 0}
reverseDict = {1: 'Rock', -1: 'Paper', 0: 'Scissors'}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if computer == you:
    print("It's a tie!")

else:
    if computer == -1 and you == 1:
        print("You lose! Paper covers Rock")
    elif computer == 1 and you == -1:
        print("You win! Paper covers Rock")
    elif computer == 0 and you == 1:
        print("You win! Rock crushes Scissors")
    elif computer == 1 and you == 0:
        print("You lose! Rock crushes Scissors")
    elif computer == 0 and you == -1:
        print("You lose! Scissors cut Paper")
    elif computer == -1 and you == 0:
        print("You win! Scissors cut Paper")
    else:
        print("Invalid input! Please enter 'r', 'p', or 's'.")
