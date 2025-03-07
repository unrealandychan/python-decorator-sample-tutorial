# This is example of classmethod

class Person:
    # This is implicitly passed to the class method as the first argument
    species = "Homo Sapiens"

    def __init__(self,name):
        self.name = name


    @classmethod
    def get_species(cls):
        return cls.species

    def get_name(self):
        return self.name

print(Person.get_species())
eddie = Person("Eddie")
print(eddie.name)
print(eddie.species)