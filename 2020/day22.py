from aocd import data

lines = iter(data.splitlines())
next(lines)
deck1 = []
for line in lines:
    if line == '':
        break
    deck1.append(int(line))
    
next(lines)
deck2 = []
for line in lines:
    if line == '':
        break
    deck2.append(int(line)) 

def draw(deck1, deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    cards = sorted([card1, card2])
    if card1 > card2:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])
        
    if len(deck1) == 0: return 2
    if len(deck2) == 0: return 1
    

def score(deck):
    total = 0
    for i, card in enumerate(reversed(deck)):
        total += (i+1) * card
    return total
    
import itertools    
def play(deck1, deck2):
    for round in itertools.count():
        print('round', round+1)
        print(1, deck1)
        print(2, deck2)
        winner = draw(deck1, deck2)
        if winner:
            break
    score1, score2 = map(score, (deck1, deck2))
    return score1, score2
    
def draw_recursive(deck1, deck2, game_id):
    if len(deck1) == 0: return 2
    if len(deck2) == 0: return 1
    
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    
    if card1 <= len(deck1) and card2 <= len(deck2):
        winner = play_recursive(deck1[:], deck2[:], game_id+1)
    else:
        winner = 1 if card1 > card2 else 2

    if winner == 1:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])
    return winner
        
GAMES = {}    
        
def play_recursive(deck1, deck2, game_id=0):
    seen = set()
    initial_state = (tuple(deck1), tuple(deck2))
    if initial_state in GAMES:
        return GAMES[initial_state]
        
    for round in itertools.count():
        #print(f'Game {game_id+1} round {round+1}')
        #print(1, deck1)
        #print(2, deck2)
        state = (tuple(deck1), tuple(deck2))
        if state in seen:
            winner = 1
            break
            
        seen.add(state)
        
        winner = draw_recursive(deck1, deck2, game_id)
        if len(deck1) == 0 or len(deck2) == 0:
            break
    print('Game', game_id+1, 'winner:', winner)
    GAMES[initial_state] = winner
    print(len(GAMES), initial_state)
    return winner
    
    
scores = play(deck1, deck2)
print('part 1', max(scores))
# part 2 (incomplete)
#print('winner', play_recursive(deck1, deck2))
#score1, score2 = map(score, (deck1, deck2))
#print(score1, score2)
