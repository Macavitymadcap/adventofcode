from copy import deepcopy

# Part 1

def strip_numbers(line):
    split_lines = line.split(' ')

    for index, string in enumerate(split_lines):
        if len(string) > 0:
            split_lines[index] = int(string)

        else:
            split_lines.pop(index)
    
    return [int(num) for num in split_lines]


def get_cards(lines):
    cards = []
    start = 0
    end = 4
    while end < len(lines):
        cards.append(
            {
                "line1": strip_numbers(lines[start]), 
                "line2": strip_numbers(lines[start+1]), 
                "line3": strip_numbers(lines[start+2]),
                "line4": strip_numbers(lines[end-1]),
                "line5": strip_numbers(lines[end])
            }
        )
        start += 6
        end += 6
    
    return cards


def check_num(num, cards):
    for card in cards:
        for line in card.values():
            for index, number in enumerate(line):
                if number == num:
                    line[index] = '*'


def print_cards(cards):
    num = 1
    for card in cards:
        print(f'\tCard {num}')
        for line in card.values():
            print(line)
        print()
        num += 1


def check_rows(card):
    for line in card:
        string = ''
        strings = [str(num) for num in card[line]]

        for num in strings:
            string += num

        if string == '*****':
            return True

    return False


def check_columns(card):
    columns = [[], [], [], [], []]
    for line in card:
        for index, column in enumerate(columns):
            column.append(str(card[line][index]))

    for column in columns:
        string = ''
        for num in column:
            string += num

        if string == '*****':
            return True

    return False

def win_bingo_round(numbers, cards):
    bingo = False
    while not bingo:
        for number in numbers:
            check_num(number, cards)

            for card in cards:
                if check_columns(card):
                    winning_numbers = []
                    for line in card.values():
                        for num in line:
                            if num != '*':
                                winning_numbers.append(num)
                    bingo = True

                    return sum(winning_numbers) * number
            
                if check_rows(card):
                    winning_numbers = []
                    for line in card.values():
                        for num in line:
                            if num != '*':
                                winning_numbers.append(num)
                    bingo = True

                    return f"{number} * {sum(winning_numbers)} = {sum(winning_numbers) * number}"

def lose_bingo_round(numbers, cards):
    bingo = True
    bingo_generator = (num for num in numbers)
    while bingo:
        if len(cards) == 1:
            while bingo:
                number = next(bingo_generator)
                check_num(number, cards)
                losing_numbers = []
                for card in cards:
                    if check_columns(card) or check_rows(card):
                        for line in card.values():
                            for num in line:
                                if num != '*':
                                    losing_numbers.append(num)

                        bingo = False
                        return f"{number} * {sum(losing_numbers)} = {number * sum(losing_numbers)}"
        
        else:
            check_num(next(bingo_generator), cards)

            for card_index, card in enumerate(cards): 
                if check_columns(card) or check_rows(card):
                    cards.pop(card_index)

if __name__ == '__main__':
    with open('day-4-input.txt', 'r') as file:
        bingo_numbers = [int(num) for num in file.readline().split(',')]
        bingo_cards = get_cards([line.strip() for line in file.readlines()[1:]])

    part1 = win_bingo_round(bingo_numbers, deepcopy(bingo_cards))
    part2 = lose_bingo_round(bingo_numbers, deepcopy(bingo_cards))
    print('Part 1:', part1)
    print('Part 2:', part2)