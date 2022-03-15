# Part 1
numbers = []

with open('day-1-input.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))

increase_count0 = 0

for index, value in enumerate(numbers):
    if index == 0:
        continue
    else:
        if value > numbers[index-1]:
            increase_count0 += 1

print(f'Increase Count 0: {increase_count0}')


# Part 2
index_count = 0
three_sum = []

while index_count < len(numbers) -2:
    three_sum.append(numbers[index_count] + numbers[index_count + 1] + numbers[index_count + 2])
    index_count += 1

increase_count1 = 0

for index, value in enumerate(three_sum):
    if index == 0:
        continue
    else:
        if value > three_sum[index-1]:
            increase_count1 += 1

print(f'Increase Count 1: {increase_count1}')
