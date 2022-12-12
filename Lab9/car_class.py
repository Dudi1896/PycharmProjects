class Car:

    #data attributes for Car class

    #init method initializing attributes
    def __int__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    #setter function to increase spee value by 5
    def accelerate(self):
            self.speed += 5

    #setter function to reduce speed value by 5
    def brake(self):
            self.speed -= 5

    #Getter method to return current speed
    def getspeed(self):
        return self.speed

