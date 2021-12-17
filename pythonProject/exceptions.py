print("hello")
k = 48
try:
    n = int(input("Enter the value"))
    print(k / n)
except ValueError as e:
    print("Value error", str(e))
except TypeError as e:
    print("Type error", str(e))
except Exception as e:
    print("Exception error", str(e))
finally:
    print("Finally block")
print("Block End")

try:
    n = int(input("Enter the value"))
    print(k / n)
except (ValueError, TypeError, Exception) as e:
    print("Value error", str(e))
finally:
    print("Finally block")
print("Block End")


class ValueTooLow(Exception):
    pass


def check_age(n):
    try:
        print("start...")
        raise ValueTooLow
        print("one line")
        raise ZeroDivisionError
    except:
        print("inside age")

print("hello")
k = 48
try:
    n = int(input("Enter the value"))
    if n < 18:
        raise ValueTooLow
    print("Employment")
except ValueError:
    print("Value Error")
except ValueTooLow as err:
    print("inside value too low", err)

