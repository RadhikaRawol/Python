class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3


E = Employee()
print(E.a)

E = Programmer()
print(E.a, E.b)

E = Manager()
print(E.a, E.b, E.c)