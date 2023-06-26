import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'summer', 'school',
    'computer', 'park', 'office', 'bodybuilder' 
]

set_word = random.choice(word_list)
# test words
print(f'Test: {set_word}')

tries = 6 # The artwork is divided into 6 parts 
game_over = False

board = []
for letter in set_word:
    board += "_"

while not game_over: 
    player_chose = input("Write a letter here: ").lower()
    
    for position_letter in range(len(set_word)):
        letter = set_word[position_letter]
        if letter == player_chose:
            board[position_letter] = letter
    if player_chose not in set_word:
        tries -= 1
        if tries == 0:
            game_over = True
            print("You've lost your head!")
                    
    if "_" not in board:
        game_over = True
        print("Congratulations, you have survived!")
