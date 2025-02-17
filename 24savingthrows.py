import random


def sim_norm(dc, sim_num):
    success_norm = 0
    for i in range(sim_num):
        x = random.randint(1,20)
        if x >= dc:
            success_norm += 1
    p_normal = success_norm / sim_num
    return p_normal

def sim_adv(dc, sim_num):
    success_adv = 0
    for i in range(sim_num):
        x = random.randint(1,20)
        y = random.randint(1,20)
        if x >= y:
            roll = x
        else:
            roll = y
        if roll >= dc:
            success_adv += 1
    p_adv = success_adv / sim_num
    return p_adv

def sim_disadv(dc, sim_num):
    success_dis = 0
    for i in range(sim_num):
        x = random.randint(1,20)
        y = random.randint(1,20)
        if x <= y:
            roll = x
        else:
            roll = y
        if roll >= dc:
            success_dis += 1
    p_dis = success_dis / sim_num
    return p_dis

print('|  DC   | Normal | Advantage | Disadvantage |')
print('|  5    |', sim_norm(5, 1000) , ' | ' , sim_adv(5, 1000) , '   | ' , sim_disadv(5, 1000), ' |')
print('|  10   |', sim_norm(10, 1000), ' | ', sim_adv(10, 1000), '   | ', sim_disadv(10, 1000), ' |')
print('|  15   |', sim_norm(15, 1000), ' | ', sim_adv(15, 1000), '   | ', sim_disadv(15, 1000), ' |')


    


