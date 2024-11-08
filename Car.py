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

class Car:

    def __init__(self, year, model, make, speed):
        self.__year = year
        self.__model = model
        self.__make =  make
        self.__speed = int(speed)
        print('Your vehicle is a', year, model, make)

#About the car
    def set_year(self, year):
        self.__year = year

    def set_model(self, model):
        self.__model = model

    def set_make(self, make):
        self.__make =  make

    def set_speed(self, speed):
        self.__speed = speed

    def get_year(self):
        return self.__year
    
    def get_model(self):
        return self.__model
            
    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed   
    
#acceleration set up
    def __init_subclass__(self, acceleration, brake):
        self._acceleration = acceleration      
        self._brake = brake
        Car.get_speed(5)

    def set_acceleration(self, speed):
        self.__speed = self.__speed + 5 

    def get_acceleration(self, speed):
        return self._acceleration


    def set_brake(self, speed):
        self.speed = speed - 5

    def get_brake(self, speed):
        return self._brake

car = Car("1973", 'Ford', 'Bronco', 0)
car.set_acceleration(5)
print(car.get_speed())
