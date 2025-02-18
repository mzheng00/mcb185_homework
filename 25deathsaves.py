import random

def sim_deathsave():
    failure = 0
    success = 0
    while failure < 3 and success < 3:
        roll = random.randint(1, 20)
        if roll == 1:
            failure += 2
        elif roll == 20:
            return 'revive'
        elif roll < 10:
            failure += 1
        elif roll >= 10:
            success += 1
    if failure == 3:
        return 'dead'
    elif success == 3:
        return 'success'

sim_num = 10000
num_revives = 0
num_death = 0
num_stable = 0

for i in range(sim_num):
    if sim_deathsave() == 'revive':
        num_revives += 1
    elif sim_deathsave() == 'dead':
        num_death += 1
    else:
        num_stable += 1

p_revives = num_revives / sim_num
p_death = num_death / sim_num
p_stable = num_stable / sim_num

print('Probability of Revive: ', p_revives)
print('Probability of Death: ', p_death)
print('Probability of Stabilizing: ', p_stable)