import random

for number in range(0, 20):
    number = random.randint(0, 19)
    print(number)

for x in range(10):
    for y in range(5):
        print(f'({x}. {y})')
