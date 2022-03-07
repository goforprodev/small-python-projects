import random
import string
words = ["ball","breif","talk","team"]

def random_word():
    word = random.choice(words)
    return word.upper()



def hangman():
    word = random_word()
    random_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(random_letter) > 0:
        print("You already used letters"," ".join(used_letters))
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")

        print(" ".join(word_list))
        user_letter = input("> ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in random_letter:
                random_letter.remove(user_letter)
        elif user_letter in used_letters:
            print("Letter already used by you try again!!")
        else:
            print("Invalid letter")






if __name__ == '__main__':
    hangman()