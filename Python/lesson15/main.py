from animals import *

def info(object):
    object.printInfo()

def animalSpeck(object):
    object.speck

cat = Cat("Гав", 3, "Бенгальская")
dog = Dog("Бобик", 5, "Хаски")
newcat = HomeCat("Муся", 4, "Сибирская", "Рыжия", "Вова")


newcat.printInfo()
animalSpeck(cat)
animalSpeck(dog)