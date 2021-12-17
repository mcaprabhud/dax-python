class Employee:
    def __new__(cls):
        print("inside new")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("inside __init__")
        self.name = "john"


el = Employee()
print(el)


class Car:
    no_of_tyres = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("inside init")

    def move(self, direction):
        print("{} is moving  in {} directions".format(self.name, direction))


c1 = Car("Audi", "red")
c1.move("right")


class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 5
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x


for i in Test(10):
    print(i)


def fib(n):
    numbers = []
    first, second = 0, 1
    while first < n:
        numbers.append(first)
        first, second = second, first + second
    print(numbers)


fib(5)


def fib_yield(n):
    first, second = 0, 1
    while n:
        yield first
        first, second = second, first + second
        n -= 1


print(list(fib_yield(5)))
