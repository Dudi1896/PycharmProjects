
def summation_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + summation_of_numbers(n-1)


def main():
    while True:
        input_number = int(input("\nEnter number: "))
        if input_number <= 0:
            print("please enter a positive number")
        else:
            print(f"The sum of 1 to {input_number} is {summation_of_numbers(input_number)}")


if __name__ == '__main__':
    main()
