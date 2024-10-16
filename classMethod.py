class Car:
    # Class attribute
    total_cars = 0

    # Constructor method
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1  # Increment the class attribute when a new car is created

    # Instance method
    def car_info(self):
        return f"Car: {self.brand} {self.model}"

    # Class method
    @classmethod
    def total_car_count(cls):
        return f"Total cars created: {cls.total_cars}"

# Create instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling instance methods
print(car1.car_info())  # Output: Car: Toyota Corolla
print(car2.car_info())  # Output: Car: Honda Civic

# Calling the class method using the class itself
print(Car.total_car_count())  # Output: Total cars created: 2

# Class methods can also be called using an instance, but it's more common to call them using the class
print(car1.total_car_count())  # Output: Total cars created: 2
