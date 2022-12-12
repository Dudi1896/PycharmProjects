class Car:

    # data attributes for Car class
    # init method initializing attributes
    def __init__(self):
        self.year_model = int(input("What year is the car?: "))
        self.make = str(input("What model is the car?: "))
        self.speed = int(input("What s the car speed in mph?: "))

    # setter function to increase speed value by 5
    def accelerate(self):
        self.speed += 5

    # setter function to reduce speed value by 5
    def brake(self):
        self.speed -= 5

    # Getter method to return current speed
    def get_speed(self):
        return self.speed
