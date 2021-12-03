from collections import Counter
from aocd import data

def calc_power_consumption_rates(numbers):
    def get_bits(column):
        counter = Counter(column)
        if len(counter) == 1: 
            return column[0], column[0]
            
        if counter['1'] == counter['0']:
            return '1', '0'
        else:
            (most_common, _), (least_common, _) = counter.most_common()
            return most_common, least_common

    columns = zip(*numbers)
    column_bits = [get_bits(column) for column in columns]
    gamma, epsilon = map(''.join, zip(*column_bits))
    return gamma, epsilon

def calc_rating(numbers, rate_index=0):
    i = 0
    while len(numbers) > 1:
        consumption_rates = calc_power_consumption_rates(numbers)
        rate = consumption_rates[rate_index]
        numbers = [number for number in numbers if number[i] == rate[i]]
        i += 1
    return int(numbers[0], 2)


numbers = [line for line in data.splitlines()]

gamma, epsilon = calc_power_consumption_rates(numbers)
print('part 1', int(gamma, 2) * int(epsilon, 2))
print('part 2', calc_rating(numbers, 0) * calc_rating(numbers, 1))
