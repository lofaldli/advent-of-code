from aocd import data

shape = {
    "A": 1, "B": 2, "C": 3,
    "X": 1, "Y": 2, "Z": 3,
}

def part1(rounds):
    scores = {
        "L": 0, "D": 3, "W": 6,
    }
    outcomes = {
        "A": {"X": "D", "Y": "W", "Z": "L"},
        "B": {"X": "L", "Y": "D", "Z": "W"},
        "C": {"X": "W", "Y": "L", "Z": "D"},
    }
    total = 0
    for opponent, player in rounds:
        outcome = outcomes[opponent][player]
        total += shape[player] + scores[outcome]
    return total

def part2(rounds):
    outcome = {
        "X": 0, "Y": 3, "Z": 6
    }
    choices = {
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
        "Z": {"A": "B", "B": "C", "C": "A"},
    }
    total = 0
    for opponent, result in rounds:
        player = choices[result][opponent]
        total += shape[player] + outcome[result]
    return total

rounds = [line.split() for line in data.splitlines()]

print('part 1', part1(rounds))
print('part 2', part2(rounds))
