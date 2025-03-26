"""encapsulation binds data and methods in single unit"""
#private __
#public no underscore
#protected _

class Employee:
    def __init__(self, name, salary):

        self.name = name
        
        self._salary = salary
        
        self.__password = "secret123"
    def get_name(self):
        return self.name


    def get_salary(self):
        return self._salary

    
    def get_password(self):
        return self.__password

    
    def __display_password(self):
        print(f"Password is {self.__password}")


employee = Employee("John", 50000)
print(employee.get_name())  
print(employee.get_salary())  
print(employee.get_password()) 


