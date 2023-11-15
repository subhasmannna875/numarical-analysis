#Remove the loop using the in operator membership expression
L = [2 ** i for i in range(7)]
X = 5

if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')
