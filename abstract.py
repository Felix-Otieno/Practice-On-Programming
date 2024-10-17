from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def sound(self):
        pass
    
    # Concrete method (can be used directly by subclasses)
    def sleep(self):
        print("This animal is sleeping.")

# Subclass 1 (inherits from Animal and implements sound method)
class Dog(Animal):
    def sound(self):
        print("Dog barks!")

# Subclass 2 (inherits from Animal and implements sound method)
class Cat(Animal):
    def sound(self):
        print("Cat meows!")

# Instantiate objects of subclasses
dog = Dog()
cat = Cat()

# Call methods
dog.sound()  # Output: Dog barks!
cat.sound()  # Output: Cat meows!
dog.sleep()  # Output: This animal is sleeping.
cat.sleep()  # Output: This animal is sleeping.
