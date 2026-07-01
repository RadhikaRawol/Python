class Employee:
    company ="LIC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")
        
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language:{self.language}")
 
class Programmer(Employee, Coder):
     company ="accenture"
     def showLanguage(self):
         print(f"The name is {self.company} and she is good with{self.language}language")
         
         
a = Employee()
b = Programmer()
b.show()
b.printLanguages()
b.showLanguages()
      