day = input('Enter The day of the week(Mon - Sun): ').lower()

match day:
    case 'monday':
        print('Monday sucks')
    case 'tuesday':
        print('Everybody loves Tueday')
    case 'wednesday':
        print('Weekend is closer')
    case 'thursday':
        print('Weekend loading')
    case 'friday':
        print('TGIF')
    case 'saturday':
        print('Today is for cleaning up')
    case 'sunday':
        print('Hope you\'re going to church?')
    case _:
        print('This is not a day of the week')
