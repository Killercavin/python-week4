class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello my naame is {self.name}, I'm a {self.gender} with {self.age} years old.")

# Create an instance of the Person class
person1 = Person("John", 30, "male")

# Call the introduce method
person1.introduce()