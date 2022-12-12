# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #4
# Author: Denzel Udemba
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.
import random

while True:
    userChoice = int(input('Rock[1] Paper[2] Scissors[3]\nPlease chose from the '
                           'following integer options above: '))
    compChoice = int(random.randrange(1, 3))
    print(f'Comp has chosen {compChoice}')
    print(f'User has chosen {userChoice}')

    if compChoice == userChoice:
        print("It is a tie")
    elif userChoice == 1:
        if compChoice == 3:
            print("Rock[1] crushes scissors[3]! Therefore you win")
        else:
            print("You lose")
    elif userChoice == 2:
        if compChoice == 1:
            print(f'Paper[2] beats Rock[1]! Therefore you win')
        else:
            print('You lost')
    elif userChoice == 3:
        if compChoice == 2:
            print(f'Scissors[3] beats Paper[2]! Therefore you win')
        else:
            print('You lost')

    replayGame = input("Play Again? (y/n): ")
    if replayGame.lower() != "y":
        break

