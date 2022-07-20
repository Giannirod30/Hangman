import random
import string

from words import words



def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower()


def hangman_game():
    word = get_word(words)
    word_letters = set(word)
    alaphabet = set(string.ascii_lowercase) #gives lowercase letters of the words in 'words'
    used_letters = set()

    lives = 7

    #this section gets user input
    while len(word_letters) > 0 and lives > 0:
        print('Lives left:', lives, ' letters used are: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word status: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alaphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print('You have already used that letter.')

        else:
            print('Invalid letter choice')

    if lives == 0:
        print('Game over')
    else:
        print('You win!!!')

hangman_game()