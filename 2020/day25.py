from aocd import data

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject_number
        value = value % 20201227
        #print(value)
    return value
        
def inverse_transform(target, subject_number, max_loop_size=10000000):
    value = 1
    for loop_size in range(1, max_loop_size+1):
        value = value * subject_number
        value = value % 20201227
        if value == target:
            return loop_size
    else:
        raise ValueError
        
card_key, door_key = map(int, data.splitlines())

card_loop_size = inverse_transform(card_key, 7)

secret = transform(door_key, card_loop_size)
print(secret)

#card_key = transform(7, 8)
#door_key = transform(7, 11)

#print(transform(door_key, 8))
#print(transform(card_key, 11))
