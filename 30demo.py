s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())

print(s.replace('o',''))
print(s.replace('o','').replace('r','i'))

import math

print(f'{math.pi}')
print(f'{math.pi:.3f}') # 3 fixed digits after deciaml
print(f'{1e6 * math.pi:e}') # exponent notation
print(f'{"hello world":>20}') # spaces in front of hello world
print(f'{"hello world":.>20}') # dots in front of hello world
print(f'{20:<10} {10}') # '20' then spaces the '10'

print('{} {:.3f}'.format('str.format', math.pi)) # 'str.format' then pi with 3 digits after decimal
print('%s %.3f' % ('printf', math.pi)) # 'printf' then pi with 3 after decimal

# Indexes

seq = 'GAATTC'
print(seq[0], seq[1]) # G A
print(seq[-1]) # C

for nt in seq: #iterate through char in seq
    print(nt, end = '') # need to add end = '' or else it will print one character per line
print()

for i in range(len(seq)):
    print(i, seq[i]) #prints the index and the char at the index

# Slices

s = 'ABCEDFGHIJ'
print(s[0:5]) # prints the index 0 through 5, so first 5 char
print(s[0:8:2]) # skips every two char 'ACDG'
print(s[:5]) # shortcut for starting from beginning
print(s[5:]) # shortcut for starting from the 5th char to the end
# s[0] same thing as s[0:1], slice that starts at zero-th element and ends before the first

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3): # slice a string into codons
    codon = dna[i:i+3]
    print(i, codon) # prints the index and the codon that is at the index

# Tuples

tax = ('Homo', 'sapiens', 9606)
print(tax) # prints '('Homo', 'sapiens', 9606)'
# you cannot change the content by using the indices
print(tax[0]) # prints the thing at index 0 'Homo'
print(tax[::-1]) # prints the tuple in reverse

# enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts): # tidier way of doing range(len(nts))
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

for nt, name in zip(nts, names): # tidier way of printing both nt and name
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)): # tiider way for printing the index, nt and name
    print(i, nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G' # changing the element at index 2 from C to G
print(nts)

nts.append('C') # adding a C to the list
print(nts)

last = nts.pop() # removes the last element from the lsit
print(last)

nts.sort() # sorts the elements based on ASCII
print(nts)
nts.sort(reverse = True) # reverses the list
print(nts)

nucleotides = nts # another name for the same list, changes occur in both
nucleotides.append('C') 
nucleotides.sort()
print(nts, nucleotides)

items = list() # creating a empty list
print(items)
items.append('eggs') # adding eggs to the list
print(items)

stuff = [] # creating empty list
stuff.append(3) # adding 3 to list
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVZ'
print(alph)
aas = list(alph) # puts each char into the list
print(aas)

# split() and join()

text = 'good day        to you'
words = text.split() # splits the string up at any number of spaces and adds them to a list
print(words)

line = '1.41,2.72,3.14'
print(line.split(',')) # splits each number at a ',' and adds them to a lsit

s = '-'.join(aas) # puts a '-' between each letter
print(s)
s = ''.join(aas) # gets rid of the dashes
print(s)

# Searching

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Practice problem: write a function that returns the minimum value of a list
def minimum(list):
    min_val = list[0]
    for i in list[1:]:
        if i < min_val:
            min_val = i
    return min_val

# Write a function that returns both the minimum and maximum values of a list
def min_and_max(list):
    min_val = list[0]
    max_val = list[0]
    for i in list[1:]:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val

# Write a function that returns the mean of the values in a list
def mean(list):
    sum = 0
    mean_val = 0
    for i in list:
        sum += i
    mean_val = sum / len(list)
    return mean_val

import math
# Write a function that computes the entropy of a probability distribution
def entropy_of_prob(list):
    h = 0 
    for i in list:
        h -= i * math.log2(i)
    return h

# Write a function that computes the Kullback-Leibler distance between two sets of probability distributions

def kl_divergence(list1, list2):
    kl = 0
    for i, j in list1:
            kl += i * math.log2((i / j)) 
    return kl

import sys
print(sys.argv)

print('xy'.join(list('ABCDE'))[4:8])

