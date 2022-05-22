# class Dog:
#     species = "Canis familiaris"
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         pass


# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#     def fullname(self):
#         print('{}{}'.format(self.first, self.last))
#         return
#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)

# emp_1 = Employee('Corey','Schafer',50000)
# emp_2 = Employee('Test','User', 60000)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


from typing_extensions import Self


class Car:  
    

    def __init__(self, name: str, color: str, doors: int, auto_transmission: bool, max_velocity: int):
        self.color = color
        self.name = name
        self.doors = doors 
        self.max_velocity = max_velocity
        if auto_transmission:
            print('auto')
        else:
            print('manual')
        self.auto_transmission = auto_transmission 
        

    def drive(self, velocity: int) -> Self:
        print(f'{self.name} driving at velocity {velocity}')
        return self

    def stop(self) -> Self:
        print(f"{self.name} stops")
        return self

    def changeColor(self, color) -> Self:
        self.color = color
        return self


bmw = Car('bmw','Black', 4, True, 200)
audi = Car('audi','White', 4, True, 220)
nissan = Car('nissan','Grey', 2, False, 250)

bmw.drive(120).stop().changeColor("White")
audi.drive(150).stop().changeColor("Blue")
nissan.drive(100).stop().changeColor("Grey")












