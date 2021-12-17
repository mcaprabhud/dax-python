s = set()
print(s)
print(type(s))

s = {1, 2, 3, 4, 5, 6, 6}
print(s)
print(type(s))


def fn_print():
    print("hello")
    print("Welcome to python")
    print("your age is 40")


fn_print()


def factorial(number):
    print(number)
    return number if number == 0 else number * factorial(number-1)
    # if number == 0:
    #     return
    # else:
    #     return number * factorial(number-1)


print(factorial(5))


def greeting(name, age):
    """
    this function greets with age
    :param name: string
    :param age: age
    :return:
    """
    print("your age", age)
    print("your name", name)


greeting("Prabhanjan", 40)

help(greeting)


def discount(total, discount, *args, ph = '897', addr = 'test addr'):
    print(total, discount)
    for i in args:
        print(i)
    print(f'{ph} {addr}')


discount(10, 20, 1, 2, 3, 4)


def discount(total, discount, *args, **kwargs):
    print(total, discount)
    for i in args:
        print(i)
    print('%s %s' % (kwargs['ph'], kwargs['addr']))


discount(10, 20, 1, 2, 3, 4, ph='456', addr='test')

x = lambda y: y**2
print(x(8))


def square(x):
    return x**2


print(list(map(square, (2, 3, 4, 5))))

print(list(map(lambda x: x**2, (2, 4, 6, 8))))

print([word.upper() for word in ['python', 'is', 'good']])


def outer():
    j = 10
    i = 8

    def inner():
        print('inner')

    def inner2():
        print('inner2')

    return inner, inner2


print(outer())
