# 11oligo.py Michelle Zheng

# function that returns the oligo melting temp of the given # of As, Cs, Gs, and Ts

def tm(A,C,G,T):
	if A+T+C+G <= 13:
		x = (A+T)*2 + (G+C)*4
		return x
	elif A+T+C+G > 13:
		x = 64.9 + 41*(G+C-16.4)/(A+T+G+C)
		return x

print(tm(5,7,3,4))
print(tm(12,3,9,5))
print(tm(1,2,1,3))