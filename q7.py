class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year):
        """Initialize the Car object with make, model, and year.""" # all car will have to fulfill these 3 parameters.
        self.make = make #make = data from Self.make
        self.model = model #model = data from Self.model
        self.year = year #year = data from Self.year

    def describe_car(self):
        """Prints the car's information in 'Year Make Model' format."""
        print(f"{self.year} {self.make} {self.model}") # formatted to (year, make, model)


# Task 2
# Create an instance of the Car class with the given attributes and call describe_car method
# - Make: Toyota, Model: Corolla, Year: 2020
car_instance = Car("Toyota", "Corolla", 2020) # declare value and fulfill the 3 parameters
#car_instance = Car("Honda", "Fit", 2023), will need to change this is a list to store multiple cars

# Calling the describe_car method
car_instance.describe_car()  #  print command in describe car method.