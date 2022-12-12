# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #5
# Author:  Denzel Udemba
#Assume you have two files containing a series of integers
# named wswinners.txt and numbers1.txt. Write a program that calculates
# the average of all the numbers stored in the files and handles 2 exceptions.
# Write code to process each file: Calculate the average Test for the following errors:
# any IOError exceptions that are raised when the file is opened and data is read from it.
# any ValueError exceptions that are raised when the items that are read from the file are
def process_file():
    sum = 0
    file_name = input("Input file for processing: ")

    with open(file_name, 'r') as file_object, open('output.txt', 'w') as outp:
       for line in file_object:
           try:
               num = float(line)
               sum += num
           except ValueError:
               outp.write('This is not a number: ')
               print(f'This is not a number: {line}')
               outp.write(line)
       outp.write('\nAverage: ' + str(sum))
    print(f'Average: {format(sum)}')


def main():
    while True:
        try:
            process_file()
        except FileNotFoundError:
            msg = "Sorry, the file does not exist."
            print(msg)

        replay_code = input("Read another file? (y/n): ")
        if replay_code.lower() != "y":
            break


if __name__ == "__main__":
    main()