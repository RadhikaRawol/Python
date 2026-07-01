class Employee:
    language = "Python" #this is a class attributes
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")
    
    @staticmethod    
    def greet(self):
        print("Good Morning")   
    
Radha = Employee()
#Radha.language = "Java" # This is instance attribute
Radha.greet()
Radha.getInfo()
#Employee.getInfo(Radha)
