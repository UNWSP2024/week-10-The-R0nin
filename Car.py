# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  
# These values should be assigned to the object's __year_model and __make data attributes.  
# It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute 
# each time it it called.
# The brake method should subtract 5 from the speed data attribute 
# each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  
#After each call to the accelerate method, get the current speed of the car and display it.  
#The call the brake method.  After each call 
# to the brake method, get the current speed of the car and display it.
speed_up = 0
class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make =  make
        self.__speed = speed
#About the car
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make =  make

    def set_speed(self, speed):
        self.__speed = speed

    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
#acceleration set up
    while speed_up > 5:
        def __init_subclass__(self, acceleration, brake) -> None:
            self._acceleration = acceleration
            self._brake = brake

        def set_acceleration(self, speed):
            self.speed =  speed + 5 

        def get_acceleration(self, speed):
            print('Current seep is:',self.__speed)
            return self._acceleration
        speed_up = speed_up + 1

    def set_brake(self, speed):
        self.speed = speed - 5

    def get_brake(self, speed):
        print(self.__speed)
        return self._brake
