RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(6):
    if i == 0 or i == 5:
        print(f'{RED}{"  " * (15)}{END}')
    elif i == 1 or i == 4:
        print(f'{WHITE}{"  " * (15)}{END}') 
    elif i == 2 or i == 3:
        print(f'{BLUE}{"  " * (15)}{END}') 