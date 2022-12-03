import re
from datetime import datetime, timedelta
from collections import defaultdict

from aocd import data
    
events = dict()
for line in data.splitlines():
    time, action = line.split(']', maxsplit=1)
    time = datetime.strptime(time.strip('['), '%Y-%m-%d %H:%M')
    events[time] = action
    
id = None
last_time = None
sleep = dict()
for time in sorted(events.keys()):
    action = events[time]
    if 'falls' in action:
        last_time = time
    elif 'wakes' in action:
        t = last_time
        sleep.setdefault(id, [0 for _ in range(60)])
        while t < time:    
            sleep[id][t.minute%60] += 1
            t += timedelta(minutes=1)
    else:
        mo = re.search(r'-?\d+', action)
        id = int(mo.group(0))
    
    
longest = sum(list(sleep.values())[0])
longest_id = list(sleep.keys())[0]
max_min = max(list(sleep.values())[0])
max_min_id = list(sleep.keys())[0]
for id, mins in sleep.items():
    if sum(mins) > longest:
        longest = sum(mins)
        longest_id = id
    if max(mins) > max_min:
        max_min = max(mins)
        max_min_id = id

mins = sleep[longest_id]
print('part 1', longest_id * mins.index(max(mins)))
mins = sleep[max_min_id]
print('part 2', max_min_id * mins.index(max(mins)))

