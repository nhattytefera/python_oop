class Person:
    species = "Homo sapiens"

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

# Update the class attribute
Person.set_species("Homo roboticus")
print(Person.species)  # Output: Homo roboticus
