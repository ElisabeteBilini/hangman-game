import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'Summer', 'school'
]

set_word = random.choice(word_list)
print(f'Test: {set_word}')

player_chose = input("Write a letter here: ").lower()

for letter in set_word:
    if letter == player_chose:
        print('Perfect')
    else:
        print('Try again')