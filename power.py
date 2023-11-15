# performance improvement by moving the 2 ** X expression outside the loop
L = []
X = 5
power_of_X = 2 ** X  # Compute 2 ** X outside the loop

for i in range(7):
    L.append(2 ** i)

if power_of_X in L:
    print('at index', L.index(power_of_X))
else:
    print(X, 'not found')
