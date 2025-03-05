import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


def birthday_list(p, d):
    list_birthdays = []
    for i in range(p):
        list_birthdays.append(random.randint(0, d - 1))
    return list_birthdays

def find_matches(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[i] == b[j]:
                return True
    return False

num_matches = 0
for i in range(trials):
    birthdays = birthday_list(people, days)
    matches = find_matches(birthdays)
    if matches == True:
        num_matches += 1

prob_match = num_matches / trials
print(f'The probability of matching birthdays: {prob_match}')

    


