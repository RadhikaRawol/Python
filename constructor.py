class Employee:
    language = "Python" #this is a class attributes
    salary = 1200000
    
    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary =salary
        self.language =language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")
    
    @staticmethod    
    def greet(self):
        print("Good Morning")   
    
Radha = Employee("Radha" , 1300000, "Java")
#Radha.name ="Radha"
print(Radha.name, Radha.salary, Radha.language)
