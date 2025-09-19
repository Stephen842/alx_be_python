rows = 20

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()

print()

for x in range(1, rows + 1):
    print(' ' * (rows - x), end='')
    print('*' * (2 * x - 1))
