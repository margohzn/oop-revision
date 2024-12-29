
class Fruit():

    def __init__(self, color, size, shape, taste, prefrence):
        self.color = color
        self.size = size
        self.shape = shape
        self.taste = taste
        self.prefrence = prefrence

    def print_info(self):
        print(self.color)
        print(self.size)
        print(self.shape)
        print(self.taste)
        print(self.prefrence)

    #creating getter fonctions - fonctions that return value of any property
    def get_shape(self):
        return self.shape
    def get_taste(self):
        return self.taste

    #creating setter fonction - fonctions that update value or any property 
    def set_size(self, new_size):
        self.size = new_size
    def increase_prefrence(self):
        self.prefrence += 1
        print("prefrence increased")
    def decrease_prefrence(self):
        self.prefrence -= 1
        print("prefrence decreased")


orange = Fruit("orange", "medium", "round", "sweet", 3)
banana = Fruit("yellow", "medium", "curved", "sweet", 5)
orange.print_info()
print()
banana.print_info()

orange_shape = orange.get_shape()
print("\n" + orange_shape)

orange_taste = orange.get_taste()
print(orange_taste)

orange.set_size("large")
print("\nUpdated Value for orange:")
orange.increase_prefrence()
orange.print_info()

