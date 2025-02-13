import random


roll = random.randint(1, 21)
print(f'You rolled a {roll}')

possible_dc = [5, 10, 15]
dc = random.choice(possible_dc)

def savingthrow():
    if roll >= dc:
        print(f'You are safe from DC of {dc}')
    else:
        print(f'You died from a DC of {dc}')

def normal():
    x = random.randint(1,21)
    if x >= dc:
        return True

def advantage():
    x = max(random.randint(1,21), random.randint(1,21))
    if x >=dc:
        return True

def disadvantage():
    x = min(random.randint(1,21), random.randint(1,21))
    if x >= dc:
        return True

success_adv = 0
success_dis = 0
success_norm = 0

for i in range(1000):
    if advantage() == True:
        success_adv += 1
    if disadvantage() == True:
        success_dis += 1
    if normal() == True:
        success_norm += 1

p_adv = success_adv / 1000
p_dis = success_dis / 1000
p_normal = success_norm / 1000

savingthrow()
print('Probability of Success:')
print(f'Normally: {p_normal}')
print(f'With Advantage: {p_adv}')
print(f'With Disadvantage: {p_dis}')



    


