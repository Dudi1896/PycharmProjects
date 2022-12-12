# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #3
# Author: Denzel Udemba
# Develop a program a college can use to input their tuition for full time students and increase
# the cost based a percentage over a certain time period. Write a program with a loop that displays
# the projected semester tuition amount for time period entered.You will need to gather the tuition,
# percentage and time period.  It will need to display each year and what the new tuition will be.

def tuition_calculate():
    tuition_fee = float(input('Enter Student tuition fee: '))
    interest_rate = float(input('Enter the rate of interest as a decimal value: '))
    num_years = int(input('Enter how many years will be displayed: '))
    rate_acc = 1 + float(interest_rate)

    for i in range(1, num_years+1):
        tuition_fee = tuition_fee * rate_acc
        print(f'year {i}')
        print(f'New tuition cost is: {tuition_fee:.2f}')

def main():
    while True:
        tuition_calculate()

        replay_code = input("Try again? (y/n): ")
        if replay_code.lower() != "y":
            break

if __name__ == "__main__":
    main()

