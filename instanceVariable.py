class School:

    school_name = "Onyalo Biro Primary School" #class variable

    def __init__(self, name, age): # Instance variable
        self.name = name
        self.age = age

    def details(self):
        print(f"The name of the school is {self.name} and it was founded in {self.age}")
        
school_obj = School("Usiogope Primary School", 1995)

print(School.school_name)
school_obj.details()