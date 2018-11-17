class Pet(object):
    # 생성자, '__'는 private의 의미 
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def __str__(self): 
        return "%s is a %s" % (self.name, self.species) 


# Pet을 상속받음
class Dog(Pet): 
    def __init__(self, bow):
        self.bow = bow

# Pet을 상속받음
class Cat(Pet): 
    def __init__(self, miao):
        self.miao = miao