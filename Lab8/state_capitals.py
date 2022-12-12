import random

capitals_dict = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix",
                 "Arkansas": "Little Rock", "California": "Sacramento", "Colorado": "Denver",
                 "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee",
                 "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield",
                 "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
                 "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta",
                 "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "Lansing",
                 "Minnesota": "Saint Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City",
                 "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
                 "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe",
                 "NewYork": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck",
                 "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem",
                 "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "SouthCarolina": "Columbia",
                 "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin",
                 "Utah": "Salt Lake City", "Vermont": "Montpelier", "Virginia": "Richmond",
                 "Washington": "Olympia", "WestVirginia": "Charleston", "Wisconsin": "Madison",
                 "Wyoming": "Cheyenne"}


def main():
    num_correct = 0
    num_wrong = 0
    while True:
        # for item in capitals_dict:
        #     print("|STATE:| {}  |CAPITAL:| {}".format(item, capitals_dict[item]))

        rand_state = random.choice(list(capitals_dict.keys()))
        user_capital = input(f"\nWhat is the capital of {rand_state}: ").lower()

        # Random state answer
        if rand_state in capitals_dict:
            print(capitals_dict.get(rand_state))

        if user_capital == capitals_dict.get(rand_state).lower():
            num_correct += 1
            print(f"User answer {user_capital} is correct"
                  f"\ncorrect total: {num_correct}")
        else:
            num_wrong += 1
            print(f"wrong answer"
                  f"\nincorrect total: {num_wrong}")

        replay_code = input("Try again? (y/n): ")
        if replay_code.lower() != "y":
            break


if __name__ == '__main__':
    main()
