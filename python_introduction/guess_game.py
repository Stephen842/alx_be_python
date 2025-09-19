import random
print('Welcome to the Number Guessing Game1\n')

### Game Loop
while True:
    secret_number = random.randint(1, 10)
    
    while True:
        user = int(input('I\'m thinking of a number between 1 and 10. Can you guess it?: '))

        match user:
            case u if u == secret_number:
                print('Congratulations, you guessed it!')
                break
            case u if u > secret_number:
                print('Nope, your guess is too high, try again!')
            case u if u < secret_number:
                print('Nope, your guess is a bit low, Give it another shot!')
    play_again = input('Play again? (yes/no): ').lower()
    if play_again not in ['yes', 'y']:
        print('Thanks for playing! Goodbye')
        break
