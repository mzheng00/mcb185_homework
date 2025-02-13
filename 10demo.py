# 10demo.py by Michelle Zheng
import math

print("hello, again") # greeting

print(1.5e-2) # 1.5 times 10 to the power of -2

print(7 + 5) # adding

print(5 * 4) # multiplication

print(6 // 4) # integer divide

print(math.ceil(5.72)) # rounds the # up

print(math.log(98)) # x in log base e

print(math.sqrt(583)) # square root of 583

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c), sep=', ', end='\n')

# converts F to C
def temp(x):
	cel = (x-32)*(5/9)
	return cel
	
print("Celsius: ",temp(98))

#calculate the mean of 4 numbers
def mean(a,b,c,d,):
	return (a + b + c + d)/4
	
print("Mean: ",mean(6,3,6,5))
