myDict = {}
myDict_1 = dict()

myDict['key'] = 'value'

d = {'name': 'Prabhanjan', 'add': 'Pune'}

l = list()
l.append(d)
l.append(d)
print(l)

d['mainbranch'] = 'Dahanu'
print(d)

print(d.keys())
print(d.values())

for item in d:
    print(item)
    print(d[item])
    print(item, '------>', d[item])

for key, value in d.items():
    print('key: %s value: %s' % (key, value))

tup = ((2, 3, 4), 5, 6, 7, (8, 9, 10))
for i in tup:
    print(i)
    if isinstance(i, tuple):
        for j in i:
            print(j)
