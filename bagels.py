import random

#sets some constants
NUM_OF_DIGITS = 5
MAX_TRAIL = 10


def bagels():
    print('''Bagels, a deductive logic game.
    16. By Al Sweigart al@inventwithpython.com
    17.
    18. I am thinking of a {}-digit number with no repeated digits.
    19. Try to guess what it is. Here are some clues:
    20. When I say: That means:
    21. Pico One digit is correct but in the wrong position.
    22. Fermi One digit is correct and in the right position.
    23. Bagels No digit is correct.
    24.
    25. For example, if the secret number was 248 and your guess was 843, the
    26. clues would be Fermi Pico.'''.format(NUM_OF_DIGITS))

    #main game loop
    while True:
        secret_number = random_number()
        print("I have thought of a number")
        print(f"You have {MAX_TRAIL} to guess it right!!")

        num_of_times_guessed = 1
        while num_of_times_guessed < 10:
            guess = ''

            while len(guess) != NUM_OF_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_of_times_guessed} ")
                print(f"hint : Try guess a {NUM_OF_DIGITS} numbers")
                guess = input("> ")

            hints = get_hints(secret_number , guess)
            print(hints)
            num_of_times_guessed += 1

            if guess == secret_number:
                break
            if num_of_times_guessed > MAX_TRAIL:
                print("Sorry you have run out of guesses")
                print(f"The correct answer is {secret_number}")

        print("Do you wish to continue (yes or no)")


        if input("> ").lower().startswith("n"):
            break
    print("Thanks for playing !!")



def random_number():
    numbers = list("1234567890")
    random.shuffle(numbers)

    guess = ''
    for i in range(NUM_OF_DIGITS):
        guess += numbers[i]
    return guess


def get_hints(rand , guess):
    if guess == rand:
        return "Correct"

    hints = []

    for i in range(NUM_OF_DIGITS):
        if guess[i] == rand[i]:
            hints.append("Fermi")
        elif guess[i] in rand:
            hints.append("Pico")
    if len(hints) == 0:
        return "Bagels"
    else:
        hints.sort()
        return " ".join(hints)


if __name__ == '__main__':
    bagels()