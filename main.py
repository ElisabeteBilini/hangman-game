import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'summer', 'school',
    'computer', 'park', 'office', 'bodybuilder' 
]

#choosing random word
select_word = random.choice(word_list).upper()
print(select_word)

#request letter to player
letter_player = input("Type one letter: ").upper()

#Checking Letter and spaces
board = []
chances = 6

for letter in range(len(select_word)):
    board += '_'

for letter_position in range(len(select_word)):
    letter = select_word[letter_position]
    if letter == letter_player:
        board[letter_position] = letter

print(board)



































