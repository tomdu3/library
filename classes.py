
class Person:
    """Represents a person.
    
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    Methods:
        get_name(): Returns the name of the person.
        set_name(name): Sets the name of the person.
        get_age(): Returns the age of the person.
        set_age(age): Sets the age of the person.
    """
    number_of_people = 0

    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        Person.number_of_people += 1

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = age
    
    @property
    def total_people(self):
        return Person.number_of_people

    @property
    def number_of_chars(self):
        return len(self.name)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

tom = Person("Tom", 46)
terry = Person("Terry", 45)

tom.set_name("Tommy")
print(tom)

print(terry)
terry.set_age(45)
print(terry)

print(terry.total_people)
terry.name = "Terrence"
print(terry.number_of_chars)
print(terry)