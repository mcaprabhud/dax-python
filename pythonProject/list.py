import math

list_l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, list_l)))


def validate(func):
    def validator(*args, **kwargs):
        if len(args) > 1:
            if args[1] == 0:
                print("We are expecting a non-zero value")
                return None
            else:
                power = func(args[0], args[1])
                return power
        else:
            print("Invalid args")

    return validator


@validate
def my_power(x, y):
    return math.pow(x, y)


my_power(2, 0)
my_power()


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(*args, **kwargs):
        print("positional arguments are: ", args)
        print("The keyword arguments are: ", kwargs)
        function_to_decorate()
    return a_wrapper_accepting_arguments()


@a_decorator_passing_arbitrary_arguments
def function_with_no_arguments():
    print("No arguments here")


def outer(func):
    def inner(*args, **kwargs):
        print("positional args", args)
        print("Keyword args", kwargs)
        s = func(*args)
        print(s.split("#")[0])
    return inner


@outer
def func_with_arguments(a, b, c):
    print(a, b, c)
    s = "hi how are you?##$$"
    return s


func_with_arguments(1, 2, 3)

x = 8
y = 3
print(x+y, x*y, x/y, x-y)
print(x**y, x//y)
print(x | y, x & y, x >> y, x << y)


def num_count(num):
    print(len(str(num)))


num_count(123456)


def reverse_string(in_str):
    index = -1
    text = list(in_str)
    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):
        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    yield text


inStr = input("Enter a string")
for i in reverse_string(inStr):
    print(i)


def f1():
    print("hello")


def f2(a, b):
    print(a)


print(f2(f1, 10))
print(f2(f1(), 10))



