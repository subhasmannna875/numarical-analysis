# using for- else  construction
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

try:
    index = L.index(2 ** X)
    print('at index', index)
except ValueError:
    print(X, 'not found')


