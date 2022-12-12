from Lab9.car_class import Car


def main():
    while True:
        new_car = Car()

        print(f'Car is accelerating:')
        for x in range(5):
            new_car.accelerate()
            print(f"current speed: {new_car.get_speed()} mph ")

        print(f'Car is breaking:')
        for x in range(5):
            new_car.brake()
            print(f"current speed: {new_car.get_speed()} mph ")

        replay_code = input("Try again? (y/n): ")
        if replay_code.lower() != "y":
            break


if __name__ == "__main__":
    main()
