import re


def load_input():
    travels = {}

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            m = re.search('^(.+) = (\d+)', line)
            travels[m.group(1)] = int(m.group(2))

    return travels


def get_town_names(travels):
    town_names = []
    for tr in travels.keys():
        town_names.extend(re.split(' to ', tr))

    town_names = list(set(town_names))

    return town_names

def perm(l):
    if len(l) == 1:
        return [l]

    perms = []

    for i in range(len(l)):
        hold = l[i]
        remainder = l[:i] + l[i+1:]

        for p in perm(remainder):
            perms.append([hold] + p)

    return perms

def distance_between_towns(travels, t1, t2):
    dist = travels.get(f'{t1} to {t2}', None)

    if not dist:
        dist = travels.get(f'{t2} to {t1}', 0)

    return dist

def calc_shortest_travel_distance(travels, town_names_perms):
    shortest_distance = 10e9

    for town_names_perm in town_names_perms:
        total_distance = 0
        for i in range(len(town_names_perm) - 1):
            total_distance += distance_between_towns(travels,
                                                     town_names_perm[i],
                                                     town_names_perm[i+1])
        if total_distance < shortest_distance:
            shortest_distance = total_distance

        total_distance = 0

    return shortest_distance


travels = load_input()
town_names = get_town_names(travels)
town_names_permutations = perm(town_names)
shortest_dist = calc_shortest_travel_distance(travels, town_names_permutations)

print(f'The shortest path distance: {shortest_dist}')
