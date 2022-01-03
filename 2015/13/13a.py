import re
from itertools import permutations

def get_scoring():
    scoring = {}

    with open('data.txt', 'r') as f:
        data = f.readlines()

    for d in data:
        m = re.search('^(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).$', d)
        subject, action, value, neighbor  = m.groups()
        if action == 'lose':
            scoring[(subject, neighbor)] = -int(value)
        else:
            scoring[(subject, neighbor)] = int(value)

    return scoring

def get_participants(scoring):
    return set([x[0] for x in scoring.keys()])

def score_participants_perm(perm, scoring):
    score = 0
    
    for i in range(len(perm)):
        subject = perm[i]
        if i == 0:
            neighbor_a = perm[-1]
            neighbor_b = perm[i + 1]
        elif i == len(perm) - 1:
            neighbor_a = perm[i - 1]
            neighbor_b = perm[0]
        else:
            neighbor_a = perm[i - 1]
            neighbor_b = perm[i + 1]

        score += scoring[(subject, neighbor_a)] + scoring[(subject, neighbor_b)]

    return score

scoring = get_scoring()
participants = get_participants(scoring)
participants_perms = list(permutations(participants))
scores = []

for perm in participants_perms:
    score = score_participants_perm(perm, scoring)
    scores.append(score)

print(f'The happiest seating order produces the following net happiness value: {max(scores)}.')
