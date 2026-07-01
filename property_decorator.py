class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name (self,value):
       self.fname = value.split(" ")[0]
       self.fname = value.split(" ")[1]    
e = Employee()
e.a = 45

e.name = "Radha"
print(e.name)

e.show()  