import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'Summer', 'school'
]

set_word = random.choice(word_list)
print(f'Test: {set_word}')

player_chose = input("Write a letter here: ").lower()

board = []
for letter in set_word:
    board += "_"
print(board)

for position_letter in set_word:
    letter = set_word[position_letter]
    if letter == player_chose:
        board[position_letter] = letter
print(set_word[(set_word.find(player_chose))])