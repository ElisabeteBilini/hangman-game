import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'Summer', 'school'
]

set_word = random.choice(word_list)
print(f'Test: {set_word}')

while set_word: 
    player_chose = input("Write a letter here: ").lower()

    board = []
    for letter in set_word:
        board += "_"

    for position_letter in range(len(set_word)):
        letter = set_word[position_letter]
        if letter == player_chose:
            board[position_letter] = letter
    print(board)

if "_" not in board:
    set_word = True
    print("You win!")