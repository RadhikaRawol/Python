class Employee:
    company ="LIC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
#class Programmer:
#    company = "LIC_Infotech"
#    def show(self):
#        print(f"The name is {self.name} and the salary is {self.salary}")
        
#    def showLanguage(self):
#        print(f"The name is {self.name} and the language is {self.language}")  
 
class Programmer(Employee):
      company = "LIC_Infotech"

def show(self):
             print(f"The name is {self.name} and the salary is {self.salary}")      
a = Employee()
b = Programmer()

print(a.company, b.company)        
          