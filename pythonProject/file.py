import contextlib

with open("python.txt", 'rt') as f:
    c = 1
    for line in f:
        if "python" in line.lower():
            print(c, line, end='')
        c += 1


@contextlib.contextmanager
def read_only(name):
    file = open(name, "r")
    yield file
    file.close()


with read_only("python.txt") as f:
    print("Printing the file")
    print(f.read())
