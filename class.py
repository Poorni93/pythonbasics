#class and object

class Cat:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    def printcatdetail(self):
        print("cat type"+self.name+"and the cost is "+self.cost+"")

#object
cat1 = Cat("natu punnai","100")
cat2 = Cat("persion", "10000")
cat1.printcatdetail()
cat2.printcatdetail()