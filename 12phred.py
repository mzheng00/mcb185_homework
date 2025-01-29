# 12phred.py Michelle Zheng
import math

# function that turns the ASCII character to probability
def char_to_prob(a):
	num = ord(a)-33
	error = 10**(-num/10)
	return error

# function that turns the character into the probability
def prob_to_char(b):
	value = -10*math.log10(b)
	symbol = chr(int(value+33))
	return symbol
	
print(char_to_prob('A'))
print(prob_to_char(0.001))
print(char_to_prob('B'))
print(prob_to_char(0.07943))