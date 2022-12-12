# Class: CIST 2742 Python Programming I
# Term: Fall 2022
# Instructor: Chris Bishop
# Description: Solution to Lab #6
# Author: Denzel Udemba
# Download World Series File and place the file in the project
# folder for lab Write code to read the file and place it into
# a list.Write code to create a display list of teams but only
# getting unique values. Then display the list Ask user for a
# team name. Write code to count how many times the inputted team won the World Series

def file_to_list():
    file_name = input("Input file name for processing: ")
    with open(file_name, 'r') as file_object:
        team_list = []
        for x in file_object:
            team_list.append(x.replace("\n", ""))

#       creates a new list with only unique values
        unique_list = [*set(team_list)]
        search_unique(unique_list)
        search_input(team_list, team_name=input('Enter the name of a team: '))

def search_unique(unique):
    for unique_teams in unique:
        print(unique_teams)

def search_input(search_list, team_name):
    print(f'The {team_name} won the world series'
          f' {search_list.count(team_name)} times between 1903 & 2021')

def main():
    while True:
        try:
            file_to_list()
        finally:
            replay_code = input("Read another file? (y/n): ")
        if replay_code.lower() != "y":
            break

if __name__ == "__main__":
    main()
