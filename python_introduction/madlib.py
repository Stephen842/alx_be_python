print('Welcome to Mad Libs, Let\'s create a story together\n')

print(f'''
On a beautiful ___ day, I went to the zoo.
I saw a funny ___ monkey swinging from the trees.
Then, I spotted a majestic ___ lion lounging in the sun.
What a wild and ___  experience! 
''')

fill_1 = input('fill in the gap: ')
fill_2 = input('fill in the gap: ')
fill_3 = input('fill in the gap: ')
fill_4 = input('fill in the gap: ')
fill_5 = ''

if fill_3 in ['fierce', 'huge', 'mighty']:
    fill_5 = 'scary'
elif fill_3 in ['sweet', 'beautiful', 'intriguing']:
    fill_5 = 'gracious'
else: 
    fill_5 = 'joyful'


story = f'''
On a beautiful {fill_1}  day, I went to the zoo.
I saw a funny {fill_2} monkey swinging from the trees.
Then, I spotted a majestic {fill_3} lion lounging in the sun.
What a wild, {fill_4} and {fill_5} experience!')
'''

print('\nThis is your Mad Libs story')

print(story)
