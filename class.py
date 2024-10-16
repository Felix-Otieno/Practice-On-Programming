class Person:
    def __init__(self, name, sex, profession):
         self.name = name
         self.sex = sex
         self.profession = profession
    
    def work(self):
         print(f"{self.name} is a {self.sex} and she is a {self.profession}. She lives in Kumpala.")
    
person_obj = Person("Alice Wakithomo", "woman", "teacher")
person_obj.work()