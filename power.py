#Use a for loop and list append method to generate the powers-of-2 list
L = []
X = 5

for i in range(7):
    L.append(2 ** i)

if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')
