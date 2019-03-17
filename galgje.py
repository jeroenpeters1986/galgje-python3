import random

WORDLIST = ["speeltje", "babystoel", "ballon", "gesodemieter", "raspberry", "kantoorwerk", "biertjes", "zwembad",
            "babyfoon", "smartphone", "moestuin", "telefoon", "camera", "zonnebrand", "sleutel", "behang", "stelten",
            "banketbakker", "slagroom", "muziek", "gitaarspel", "snaren", "konijntje", "strandhuis", "vrolijk"]


def start_guessing(game_word):
    """ Guess the word until it's solved or the player ran out of guesses """
    tries_left = 10
    game_started = False
    answer = "-" * len(game_word)
    guess_result = "Heel veel succes!"

    while tries_left > 0 and not answer == game_word:
    
        if game_started:
            clear_screen()
            draw_hangman(tries_left)
        
        game_started = True

        print("\n Woord: {0}\n\n {1}\n\n".format(answer, guess_result))
        print(" Je mag nog {0} letters raden".format(tries_left))
        guess = input(" Geef een letter op: ")

        if len(guess) != 1:
            print(" Geef precies 1 letter tegelijk op!")
        elif guess in game_word:
            guess_result = "Ja, die letter zit in het woord!"
            answer = update_answer(game_word, answer, guess)
        else:
            guess_result = "Helaas! Die letter zit er niet in."
            tries_left -= 1

    clear_screen()
    if tries_left == 0:
        draw_hangman(tries_left)
        print(" Je hangt!\n\ Oeps! Je had geen beurten meer!\n Het juiste woord was: {}\n".format(game_word))
        print(" Om nogmaals te spelen kun je het programma gewoon nogmaals uitvoeren.\n")
    else:
        print("    _\n   (_)\n   \|/\n    |\n   / \\\n\n")
        print(" Nice, gefeliciteerd! Het juiste woord was: {}\n".format(game_word))


def update_answer(word, answer, guess):
    """ Update the answer so the user can see his/her progress in solving """
    result = ""
    for i, letter in enumerate(word):
        if letter == guess:
            result = result + guess
        else:
            result = result + answer[i]
    return "{0}".format(result)


def draw_hangman(stage):
    """ Essentially.. this is ASCII art, very poor performed """
    HANGMAN_STAGES = {
        10: "",
        9: "\n\n\n\n\n\n\n _____",
        8: "\n  |\n  |\n  |\n  |\n  |\n  |\n _|___",
        7: "  ________\n  |/ \n  |\n  |\n  |\n  |\n  |\n _|___",
        6: "  ________\n  |/      |\n  |      (_)\n  |\n  |\n  |\n  |\n _|___",
        5: "  ________\n  |/      |\n  |      (_)\n  |       |\n  |\n  |\n  |\n _|___",
        4: "  ________\n  |/      |\n  |      (_)\n  |      \|\n  |\n  |\n  |\n _|___",
        3: "  ________\n  |/      |\n  |      (_)\n  |      \|/\n  |\n  |\n  |\n _|___",
        2: "  ________\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |\n  |\n _|___",   
        1: "  ________\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |      /\n  |\n _|___",
        0: "  ________\n  |/      |\n  |      (_)\n  |      \|/\n  |       |\n  |      / \\\n  |\n _|___",
    }

    if stage in HANGMAN_STAGES:
        print(HANGMAN_STAGES[stage] + "\n")


def clear_screen():
    """ Try to fetch the screenheight and "clear" it by printing empty lines """
    try:
        import fcntl, termios, struct
        screen_height = struct.unpack('hh', fcntl.ioctl(0, termios.TIOCGWINSZ, '1234'))[0]
    except:
        screen_height = 80
    
    print("\n" * screen_height)


def main():
    """ Just startup the game after a short welcome """
    game_word = random.choice(WORDLIST)
    clear_screen()
    print("   ____         _          _\n  / ___|  __ _ | |  __ _  (_)  ___\n | |  _  / _` || | / _` | | | / _ \\\n \
        | |_| || (_| || || (_| | | ||  __/\n  \____| \__,_||_| \__, |_/ | \___|\n                   |___/|__/\n\n")
    print("Welkom bij Galgje!\n\n\n Probeer het woord te raden binnen 10 beurten.")
    print(" Ik heb een woord in gedachten.")
    start_guessing(game_word)


if __name__ == "__main__":
    main()