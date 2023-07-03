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
        
player_01 = input("Player 1, enter your name: ").upper()
player_02 = input("Player 2, enter your name: ").upper()

atual_player = player_01

while not game_over:
    #identifying player
    print('Player :' + ''.join(board))
    print(f"{atual_player}'s turn.")

    #request letter to player
    letter_player = input("Type one letter: ").upper()

    #Checking Letter and spaces
    has_letter = False
    for letter_position in range(len(select_word)):
        letter = select_word[letter_position]
        if letter == letter_player:
            board[letter_position] = letter
            has_letter = True

    if not has_letter:
        chances -= 1
        if chances == 0:
            game_over = True
            print("Beware, words can also kill! You lose.")
            print(f'{atual_player} lost the game.')
            break

    if blanks not in board:
        game_over = True
        print("Congratulation, you survive!")
        print(f'{atual_player} won the game.')
    
    if atual_player == player_01:
        atual_player = player_02
    else:
        atual_player = player_01
    print(body_pieces[chances])































