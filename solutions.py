def read_calories():
    with open ('calories.txt') as f:
        return f.readlines()

def most_calories(lines):
    max = 0
    total_per_elf = 0
    for line in lines:
        if line == '\n':
            if total_per_elf > max:
                max = total_per_elf

            total_per_elf = 0
            continue

        total_per_elf += int(line.split('\n')[0])

def top_three_calories(lines):
    totals = []
    total_per_elf = 0
    for line in lines:
        if line == '\n':
            totals.append(total_per_elf)
            total_per_elf = 0
            continue

        total_per_elf += int(line.split('\n')[0])

    return sorted(totals)[-3:]

ROCK_PAPER_SCISSORS = {
        'rock': {'values': ['A', 'X'], 'beats': 'scissors', 'points': 1},
        'paper': {'values': ['B', 'Y'], 'beats': 'rock', 'points': 2},
        'scissors': {'values': ['C', 'Z'], 'beats': 'paper', 'points': 3},
    }


def rock_paper_scissors_part_one():
    with open ('rockpaperscissors.txt') as f:
        lines = f.readlines()

    your_score = 0
    for line in lines:
        opp_play = [k for k, v in ROCK_PAPER_SCISSORS.items() if line.split(' ')[0] in v['values']][0]
        your_play = [k for k, v in ROCK_PAPER_SCISSORS.items() if line.split(' ')[1].strip() in v['values']][0]
        shape_points = ROCK_PAPER_SCISSORS[your_play]['points']

        if opp_play == ROCK_PAPER_SCISSORS[your_play]['beats']:
            your_score += (6 + shape_points)
        elif opp_play == your_play:
            your_score += (3 + shape_points)
        else:
            your_score += (0  + shape_points)

    return your_score

def rock_paper_scissors_part_two():
    with open ('rockpaperscissors.txt') as f:
        lines = f.readlines()

    your_score = 0
    for line in lines:
        opp_play = [k for k, v in ROCK_PAPER_SCISSORS.items() if line.split(' ')[0] in v['values']][0]
        your_play = line.split(' ')[1].strip()
        if your_play == 'X':
            shape = ROCK_PAPER_SCISSORS[opp_play]['beats']
            your_score += 0
        elif your_play == 'Y':
            shape = opp_play
            your_score  += 3
        else:
            shape = [k for k, v in ROCK_PAPER_SCISSORS.items() if v['beats'] == opp_play][0]
            your_score += 6

        shape_points = ROCK_PAPER_SCISSORS[shape]['points']
        your_score += shape_points

    return your_score

def priority_score(letter):
    alphabet = {}
    i = 1
    for char in list(map(chr, range(97, 123))):
        alphabet[char] = i
        i += 1

    for char in list(map(chr, range(65, 91))):
        alphabet[char] = i
        i += 1

    return alphabet[letter]

def rucksack_reorganisation():
    with open ('rucksack.txt') as f:
        lines = f.readlines()

    total_priority = 0
    for line in lines:
            items = list(line.strip())
            rucksack_size = len(items)/2
            rucksack_one = items[:int(rucksack_size)]
            rucksack_two =  items[int(rucksack_size):]
            common_item = next(iter(set(rucksack_one).intersection(rucksack_two)))
            total_priority += priority_score(common_item)

    return total_priority

def rucksack_badges():
    with open ('rucksack.txt') as f:
        lines = f.readlines()

    groups = []
    for i in range(0, len(lines), 3):
        groups.append([line.strip() for line in lines[i:i+3]])

    total_priority =  0
    for group in groups:
        badge = next(iter(set(group[0]).intersection(group[1], group[2])))
        total_priority += priority_score(badge)

    return total_priority
