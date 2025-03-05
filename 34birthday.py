import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def calendar_bdays(p, d):
    calendar = [0] * d
    for i in range(p):
        birthday = random.randint(0, d - 1)
        calendar[birthday] += 1
    return calendar


def find_matches(b):
    for i in b:
        if i > 1:
            return True
    return False

num_matches = 0
for i in range(trials):
    birthdays = calendar_bdays(people, days)
    matches = find_matches(birthdays)
    if matches == True:
        num_matches += 1

prob_match = num_matches / trials
print(f'The probability of matching birthdays: {prob_match}')