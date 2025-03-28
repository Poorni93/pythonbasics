#polymorphism
""" types:complile time (method overloading), runtime polymorphism(method overriding)"""
class Parent:
    def about(self):
        print("parent is calling")

class Child:
    def about(self):
        print("child is calling")

person = Child()
person.about()

