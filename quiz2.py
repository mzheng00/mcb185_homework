import math

# checks which number out of 4 is the max number
def max(a,b,c,d):
	if a >= b and a >= c and a >= d:
		return a
	elif b >= a and b >= c and b >= d:
		return b
	elif c >= a and c >= b and c >= d:
		return c
	else:
		return d

print(max(5,7,9,3))


# checks if a number is valid probability
def valid_prob(a):
	if a < 1:
		return True
	return False

print(valid_prob(0.478))
print(valid_prob(5.830))

# finds the geometric mean of 4 numbers
def geo_mean(a,b,c,d):
	mean = math.sqrt(a + b + c + d)
	return mean
	
print(geo_mean(4, 6, 2, 8))
print(geo_mean(8, 1, 14, 7))