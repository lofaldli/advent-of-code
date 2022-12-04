import re

from aocd import data

candidates = dict()
all_ingredients = list()

for line in data.splitlines():
  ingredients, allergens = line.strip(')').split(' (contains ')
  ingredients = ingredients.split()
  all_ingredients.extend(ingredients)
  
  for allergen in allergens.split(', '):
    if allergen in candidates:
      candidates[allergen] = candidates[allergen].intersection(set(ingredients))
    else:
      candidates[allergen] = set(ingredients)

all_allergens = set.union(*candidates.values())
print('part 1', sum(i not in all_allergens for i in all_ingredients))
      
decided = {}
while any(a not in decided for a in candidates):
    for a, i in candidates.items():
        if len(i) == 1 and a not in decided:
            decided[a] = next(iter(i))
        else:
            i -= set(decided.values())
            
print('part 2', ','.join(decided[k] for k in sorted(decided)))
