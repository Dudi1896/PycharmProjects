# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #X
# Author: (Student Name Here)
#
# By turning in this code, I Pledge:
# 1. That I have completed the programming assignment independently.
# 2. I have not copied the code from a student or any source.
# 3. I have not given my code to any student.



import random

ruletResult = random.randrange(0, 36)

print(f'You randomly landed on {ruletResult}')

if ruletResult == 0:
    print(f'{ruletResult} --> it means this pocket is green')
elif ruletResult <= 10:
    if ruletResult % 2 == 0:
        print(f'{ruletResult} --> this means the pocket is black')
    else:
        print(f'{ruletResult} --> this means the pocket is red')
elif ruletResult >= 11 and ruletResult <= 18:
    if ruletResult % 2 == 0:
        print(f'{ruletResult} --> this means the pocket is red')
    else:
        print(f'{ruletResult} --> this means the pocket is black')
elif ruletResult >= 19 and ruletResult <= 28:
    if ruletResult % 2 == 0:
        print(f'{ruletResult} --> this means the pocket is black')
    else:
        print(f'{ruletResult} --> this means the pocket is red')
elif ruletResult >= 29:
    if ruletResult % 2 == 0:
        print(f'{ruletResult} --> this means the pocket is red')
    else:
        print(f'{ruletResult} --> this means the pocket is black')

