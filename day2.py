# Read the input
with open('day-2-input.txt', 'r') as file:
    data = [line.strip() for line in file]

# Part 1
forwards = [int(string.replace('forward', '').strip()) for string in data if string[0:7] =='forward']
downs = [int(string.replace('down', '').strip()) for string in data if string[0:4] =='down']
ups = [int(string.replace('up', '').strip()) for string in data if string[0:2] =='up']

forward_sum = sum(forwards)
down_sum = sum(downs)
up_some = sum(ups)

first_depth = sum(forwards) * (sum(downs) - sum(ups))
print(f'Final Depth: {first_depth}')

# Part 2
aim = 0
horizontal_position = 0
depth = 0
for line in data:
    line_list = line.split(' ')
    direction = line_list[0]
    value = int(line_list[1])
    if direction == 'down':
        aim += value

    elif direction == 'up':
        aim -= value

    else:
        horizontal_position += value
        depth += aim * value

second_depth = horizontal_position * depth

print(f'second depth: {second_depth}')

