class Parrot:

# class attribute
species = "bird"

# instance attribute
def_init_(self, name, age):
    self.name = name
    self.age = age

    #instantiate the Parrot class
    blu = Parrot ("Blu", 10)
    woo = Parrot ("Woo", 15)

    # access the class attributes
    print("Blu is a {}".format(blu.species))
    print("Woo is a {}".format(woo.species))

    # access the instance attributes
    print("{} is {} years old".format(blu.name, blu.age))
    print("{} is {} years old".format(woo.name, woo.age))

