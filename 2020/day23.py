def move(cups):
    
    current = cups[0]
    pick_up = cups[1:4]
    destination = current - 1
    if destination == 0:
        destination = len(cups)
    while destination in pick_up:
        destination -= 1
        if destination <= 0:
            destination = len(cups)
        
    cups = cups[:1] + cups[4:]
    print('current', current)
    print('pick up', pick_up)
    print('destination', destination)
    destination_index = cups.index(destination)
    cups = cups[:destination_index+1] + pick_up + cups[destination_index+1:]
    return cups[1:] + cups[:1]

data = '389125467'
data = '469217538'
cups = list(int(x) for x in data)
for _ in range(100):
    print('cups', cups)
    cups = move(cups)

    print()
    
one_index = cups.index(1)
print('part 1', ''.join(map(str, cups[one_index:] + cups[:one_index]))[1:])

# part 2 not completed
