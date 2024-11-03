import os
import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"
WHITE = 255
YELLOW = 3
BLACK = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_letters(letters, duration):
    while True:
        for letter in letters:
            clear()
            print(letter)
            time.sleep(duration)

if __name__ == "__main__":
    letters = [ f"{SET_COLOR}{YELLOW}m{' CYBER '}{END}", f"{SET_COLOR}{BLACK}m{' PUNK '}{END}" ]

    animate_letters(letters, 1)



