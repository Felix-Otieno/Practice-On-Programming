class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def details(self):
        print(f"{self.name} \n {self.max_speed} \n {self.mileage}")

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, color, brand, model):
        super().__init__(name, max_speed, mileage)
        self.color = color
        self.brand = brand
        self.model = model

    def details2(self):
        print(f"{self.name} \n {self.max_speed} \n {self.mileage} \n {self.color} \n {self.brand} \n {self.model}")

inherit_obj = Bus("cartoon", 1000, 25000, "blue", "afeloh", "liih")
inherit_obj.details()
inherit_obj.details2()