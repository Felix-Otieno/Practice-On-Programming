class Details:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def info(self):
        print(f"name: {self.name} \n salary: {self._salary}")

details_obj = Details("Felix Otieno", 200000)
details_obj.info()
print(details_obj._salary)
    