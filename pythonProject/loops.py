print('Prabhanjan')

print([i for i in range(10)])
print([i for i in range(10) if i % 2 == 0])

n = [1, 2, 3, 4, 5, 6, 7, 8]
num = input("Please enter number")
squares = [num**2 for num in n]
print(squares)

print({k: k**2 for k in range(1, 6)})

tp = (45, 77, 109, 'data', ['alex', 'john'])
print({k: tp[k] for k in range(len(tp))})

print({tp.index(v): v for v in tp})

x = 11
if x == 10:
    print("x is 10")
    print("End of block")
print("hello")

y = 11
if y == x:
    print("both are equal")
else:
    print("unequal")

for i in ('python'):
    print(i, end=' ')

for i in 'python':
    print(i)

for i in range(10):
    print(i)

x = int(input("Enter the number"))
fact = 1
for i in range(1, x+1):
    fact = fact * i
print("%d! = %d" % (x, fact))

count = 5
while count:
    print(count)
    count -= 1

tempnum = num = int(input("enter the number"))
fact = 1
while num > 0:
    fact = fact * num
    num -= 1
print(f"{tempnum}! = {fact}")

