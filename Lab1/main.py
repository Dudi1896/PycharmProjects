# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients.
# Write a program that asks the user how many cookies he or she wants
# to make, then displays the number of cups of each ingredient
# needed for the specified number of cookies.
# Execute the program and take screen capture of output.
# Submit screen capture and python(py) file via blackboard.

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)
turtle.done()




CUPS_OF_SUGAR = 0.03125
CUPS_OF_BUTTER = 0.0208333333
CUPS_OF_FLOUR = 0.0572916667

numCookies = input('\nHello, welcome to Suzies Bakery,Please'
                   ' insert the number of cookies that you would like: ')

sugarCup = int(numCookies) * float(CUPS_OF_SUGAR)
butterCup = int(numCookies) * float(CUPS_OF_BUTTER)
flourCup = int(numCookies) * float(CUPS_OF_FLOUR)

print(f'You asked for {numCookies} cookies')
print('Which Means you need the following quantity of ingredients:')
print(f'{sugarCup:.2f} Cups of Sugar')
print(f'{butterCup:.2f} Cups of Butter')
print(f'{flourCup:.2f} Cups of Flour')
