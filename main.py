import random

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'summer', 'school',
    'computer', 'park', 'office', 'bodybuilder' 
]

chances = 6 # body has 6 pieces
board = []
blanks = '_'
game_over = False

#choosing random word
select_word = random.choice(word_list).upper()
print(select_word)

for letter in range(len(select_word)):
        board += blanks

while not game_over:
    #request letter to player
    letter_player = input("Type one letter: ").upper()

    #Checking Letter and spaces
    for letter_position in range(len(select_word)):
        letter = select_word[letter_position]
        if letter == letter_player:
            board[letter_position] = letter

    print(board)

    if blanks not in board:
        game_over = True
        print("Congratulation, you survive!")


































