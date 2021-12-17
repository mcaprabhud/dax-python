from datetime import date
import copy
from dataclasses import dataclass


class A:
    pass


class B(A):
    pass


class C(B):
    pass


c = C()
print(C.mro())


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("John", 21)
person2 = Person.fromBirthYear("raj", 1998)

print(person1.age, person2.age)

print(Person.isAdult(person1.age))


l1 = [1, 2, 3, 4, [2, 3]]
l2 = copy.deepcopy(l1)

print(l1, l2)
l3 = copy.copy(l1)

print(l3)
l3[4][1] = 100

print(l1, l3)


@dataclass
class DataClassExample:
    title: str
    name: str
    phone: int


a = DataClassExample("Test", "Test", 9702799990)
b = DataClassExample("Test", "Test", 9702799990)
print(a == b)
print(a == copy.copy(a))


class NormalClassExample:

    def __init__(self, title, name, phone):
        self.title = title
        self.name = name
        self.phone = phone


a = NormalClassExample("Test", "Test", 9702799990)
b = NormalClassExample("Test", "Test", 9702799990)
print(a == b)
print(a == copy.deepcopy(a))

