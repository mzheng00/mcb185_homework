import math

t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
    
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])

#while True:
#	print('hello')
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: 
		break

i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)
	
for i in range(5):
	print(i)
	
for i in range(4, -1, -1):
	print(i)
	
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])
	
print("Practice")

def triangular(n):
	sum = 0
	for i in range(n+1):
		sum += i
	return sum

print(triangular(4))

def factorial(n):
	if n == 0:
		return 1
	fac = 1
	for i in range(1, n+1):
		fac = fac * i
	return fac

print(factorial(5))

def poisson(n, k):
	prob = n**k * math.e**-n / factorial(k)
	return prob

print(poisson(4, 6))

