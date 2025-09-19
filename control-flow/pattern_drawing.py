value = int(input('Enter the size of the pattern:'))
row = 0

while row < value:
    for x in range(value):
        print('*', end='')
    print()
    row += 1
