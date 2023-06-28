from art import body_pieces, hang, you
import random

print(hang)

word_list = [ 
    'elephant', 'guitar', 'computer', 'pizza', 'bicycle', 'diamond', 'rainbow',
    'spider', 'telescope', 'dragon', 'house', 'book', 'bed', 'summer', 'school',
    'computer', 'park', 'office', 'bodybuilder' 
]

#choosing random word
select_word = random.choice(word_list).upper()
print(select_word)

board = []
blanks = '_'
chances = 6 
game_over = False

for letter in range(len(select_word)):
        board += blanks

player_01 = input("Player 1, enter your name: ")
player_02 = input("Player 1, enter your name: ")

current_player = player_01

while not game_over:
    #request letter to player
    letter_player = input("Type one letter: ").upper()

    #Checking Letter and spaces
    for letter_position in range(len(select_word)):
        letter = select_word[letter_position]
        if letter == letter_player:
            board[letter_position] = letter
    print(board)

    if letter_player not in range(len(select_word)):
        chances -= 1
        if chances == 0:
            game_over = True
            print("Beware, words can also kill! You lose.")



    if blanks not in board:
        game_over = True
        print("Congratulation, you survive!")

    print(body_pieces[chances])































