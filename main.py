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

#Checking Letter
for letter in select_word:
    if letter == letter_player:
        print("you're right!")
    else:
        print("wrong!")






































