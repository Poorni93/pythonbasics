#inheritance allows one class to inherit the propertoes and behaviour of another class
"""single inheritance ---- one child,one parent"""
#parent
class Book:
    def __init__(self,name):
        self.name = name

    def aboutbook(self):
        print(f"book name is {self.name}")


#child
class Poeticbook(Book):
    def __init__(self, name,author):
        super().__init__(name)
        self.author = author

    def bookdetails(self):
        print(f"the book name is {self.name}and the author of the book is {self.author}")

book1 = Poeticbook("anilaadum mundril","na.muthukumar")
book1.bookdetails()
book1.aboutbook() #parent function

"""hierarchical inheritance  ----- one parent multiple children"""

#same parent used

class Book_about_freedom(Book):
    def __init__(self, name,author,year):
        super().__init__(name)
        self.author = author
        self.year = year

    def printdetail(self):
        print(f"the book name is {self.name}author is {self.author} the year is {self.year}")

book2 = Book_about_freedom("sudesa geethangal","barathiyar","1908")
book2.printdetail()

"""multiple inheritance-----mutliple parent,single child"""

class Mammal:
    def __init__(self,name):
        self.name = name

    def showmams(self):
        print(f"mammal name {self.name}")

class Animal:
    def __init__(self,species):
        self.species=species

    def printanimal(self):
        print(f"animal is{self.species}")

class Cat(Mammal,Animal):
    def __init__(self, name,species):
        super().__init__(name)
        self.species = species
    def food(self):
        print("cat drinks a milk")

cat1 = Cat("meow","cat species")
cat1.food()
cat1.showmams()
cat1.printanimal()

"""multilevel grand parent -parent- child"""

class Milkyway:
    def details(self):
        print("milkyway have a planets")

class Planets(Milkyway):
    def planetdetail(self):
        print("we have a 9 planets inside of milyway")

class Earth(Planets):
    def Earthdetails(self):
        print("earth is one of the most attractive planet")

earth = Earth()
earth.Earthdetails()
earth.planetdetail()
earth.details()

"""hybrid ----combination of multiple inheritance"""

class ImportantPlanet:
    def importants(self):
        print("the all planets are important")

class Sun(Planets,ImportantPlanet):
    def sundetails(self):
        print("sun is important for all living things and it is a first planet also")

aboutsun = Sun()
aboutsun.sundetails()
aboutsun.importants()
aboutsun.planetdetail()
aboutsun.details()