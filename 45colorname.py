# program that provides the closest official color name given some red, green, and blue values
import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
    return abs(P - Q)

with open(colorfile, 'rt') as fp:
    total_dist = 1000
    color = ''
    for line in fp:
        column = line.split()
        rgb_num = column[2].split(',')
        dist_r = dtc(int(rgb_num[0]), R)
        dist_g = dtc(int(rgb_num[1]), G)
        dist_b = dtc(int(rgb_num[2]), B)
        sum = dist_b + dist_g + dist_r
        if total_dist > sum:
            total_dist = sum
            color = column[0]

print(color)

    
    
