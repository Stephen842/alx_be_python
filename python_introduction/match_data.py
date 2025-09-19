name = input('Enter your first name: ')
age = int(input('How old are you?: '))

match (name, age):
    case (str(name), int(age)):
        print('You enterer a string for name: ', name)
        print('You entered a integer for age: ', age)

    case _:
        print('Wrong format of data type entered, please check and try again')
