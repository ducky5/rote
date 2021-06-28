# create class(base class in this context)
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    # instance(object) method
    def is_allowed(self):
        if self.age >= 18:
            return True
        else:
            return False

# create object from class
person1 = Person("Riad", "Male", 17)

print("Name:", person1.name, ", Age:", person1.age, ", Gender:", person1.gender)
print("is_allowed:", person1.is_allowed())

print()

# inheritance
# create class(derived class in this context)
class Person_special(Person):
    # method overriding
    def is_allowed(self):
        if self.age >= 17:
            return True
        else:
            return False

# create object from inheriting class
person2 = Person_special("Yassir", "Male", 17)
print("Name:", person2.name, ", Age:", person2.age, ", Gender:", person2.gender)
print("is_allowed:", person2.is_allowed())
