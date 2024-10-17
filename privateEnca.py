class Person:
    def __init__(self, name, tribe):
        self.name = name
        self.__tribe = tribe

    def details(self):
        print(f"name: {self.name} \n tribe: {self.__tribe}")  

obj = Person("MwanaWaBukulukulu", "Luo")
obj.details()
print(obj.__tribe)  
        