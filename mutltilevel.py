class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

E = Employee()
print(E.a)

E = Programmer()
print(E.a, E.b)

E = Manager()
print(E.a, E.b)