# Part 1

def get_power():
    gamma_rate_string = ''
    epsilon_rate_string = ''
    one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open('day-3-input.txt', 'r') as file:
        for line in file:
            for index, value in enumerate(line.strip()):
                if value == '0':
                    zero_count[index] += 1
                else:
                    one_count[index] += 1

    for index, value in enumerate(zero_count):
        if value > one_count[index]:
            gamma_rate_string += '0'
            epsilon_rate_string += '1'

        else:
            gamma_rate_string += '1'
            epsilon_rate_string += '0'

    gamma_rate_int = int(gamma_rate_string, 2)
    epsilon_rate_int = int(epsilon_rate_string, 2)
    power_consumption = gamma_rate_int * epsilon_rate_int

    return power_consumption

# Part 2

def get_o2_list(data, index):
    off_count = 0
    on_count = 0
    o2_list = []

    for line in data:
        if line[index] == '0':
            off_count += 1
        else:
            on_count += 1

    if on_count > off_count or on_count == off_count:
        for line in data:
            if line[index] == '1':
                o2_list.append(line)
    
    else:
        for line in data:
            if line[index] == '0':
                o2_list.append(line)
    
    return o2_list


def get_o2_rating(data):
    index = 0
    solution = get_o2_list(data, index)

    while len(solution) != 1:
        index += 1
        solution = get_o2_list(solution, index)
    
    return int(solution[0], 2)


def get_co2_list(data, index):
    off_count = 0
    on_count = 0
    co2_list = []

    for line in data:
        if line[index] == '0':
            off_count += 1
        else:
            on_count += 1

    if on_count > off_count or on_count == off_count:
        for line in data:
            if line[index] == '0':
                co2_list.append(line)
    
    else:
        for line in data:
            if line[index] == '1':
                co2_list.append(line)
    
    return co2_list


def get_co2_rating(data):
    index = 0
    solution = get_co2_list(data, index)

    while len(solution) != 1:
        index += 1
        solution = get_co2_list(solution, index)
    
    return int(solution[0], 2)


with open('day-3-input.txt', 'r') as file:
    data = [line.strip() for line in file]

oxygen_generator_rating = get_o2_rating(data)
co2_scrubber_rating = get_co2_rating(data)
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating)
