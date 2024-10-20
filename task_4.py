BLUE = '\u001b[44m'
GREEN = '\u001b[48;5;34m'
END = '\u001b[0m'

if __name__=='__main__':

    lower = []
    upper = []


    with open("sequence.txt") as file:
        array = [row.strip() for row in file]


    for i in range(len(array)):
        item = float(array[i])
        if item > 0 and item <= 5:
            lower.append(item)
        if item > 5:
            upper.append(item)

    summ = len(lower) + len(upper)


    print('процент от 5: ' f'{GREEN}{'  ' * ((int((len(lower)) / summ * 100))//2)}{END}', round((len(lower)/ summ) * 100, 2),'% - от всех чисел больше 0')
    print('процент до 5: ' f'{BLUE}{'  ' * ((int(len(upper) / summ * 100))//2)}{END}', round((len(upper)/ summ) * 100, 2),'% - от всех чисел больше 0')

    

