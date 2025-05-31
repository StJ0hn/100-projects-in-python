import random

word_list_easy = [ "cat", "house", "book", "sun", "ball", "table", "flower", "candy", "eye", "wind"]
word_list_medium = ["window", "garden", "stairs", "planet", "clock", "lantern", "pillow", "backpack", "perfume", "diamond"]
word_list_hard = ["crocodile", "labyrinth", "kilometer", "submarine", "lightning", "astronaut", "dictionary", "electrician", "archipelago", "parallelepiped"]
stages = [
    '''
     _______
    |/
    |
    |
    |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |
    |
    |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |
    |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |       |
    |       |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |      /|
    |       |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |      /
    |___
    ''',
    '''
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |      / \\
    |___
    '''
]




#Tratment of easy words
easy_words = random.choice(word_list_easy)
lenght_easy = len(easy_words)
new_easy = easy_words.replace(easy_words,"_" * lenght_easy)

#Tratment of medium words
medium_words = random.choice(word_list_medium)
lenght_medium = len(medium_words)
new_medium = medium_words.replace(medium_words,"_" * lenght_medium)

#Tratment of hard words
hard_words = random.choice(word_list_hard)
lenght_hard = len(hard_words)
new_hard = hard_words.replace(hard_words,"_" * lenght_hard)

#Choosing a dificult
dificulty = ["easy", "medium", "hard"]
choose = input("Choose a dificulty of game (Easy/Medium/Hard): ").lower()
while choose not in dificulty:
    print("Invalid choice, try again: ")
    choose = input()
    if choose == "easy" or choose == "medium" or choose == "hard":
        print("Dificulty selected: " + choose)
        break

#Picking a word from the list based on difficulty
word = ""
if choose == "easy":
    word = easy_words
elif choose == "medium":
    word = medium_words
elif choose == "hard":
    word = hard_words

#Start of game
lifes = 7
game_over = False
attempted_letters = []
while not game_over:
    print(word)
    guess = input("Guess a letter: ").lower()

    while guess in attempted_letters:
        print("Letter already chosen, try again.")
        guess = input("Guess a new letter: ").lower()

    attempted_letters.append(guess)


    if guess not in word:
        lifes -= 1
        print(stages[7 - lifes])


    display = ""
    for letter in word:
        if letter in attempted_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
    elif lifes == 0:
        game_over = True
        print("You lost.")
