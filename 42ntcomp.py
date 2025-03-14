# calculates the composition of nucleotides in a FASTA file

import sys
import mcb185
'''
# gc composition of FASTA file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    gc = 0
    for nt in seq:
        if nt == 'C' or nt == 'G': gc += 1
    print(name, gc/len(seq))

# all nucleotides of FASTA file

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    A = 0
    C = 0
    G = 0
    T = 0
    N = 0
    for nt in seq:
        if nt == 'A':
            A += 1
        elif nt == 'C':
            C += 1
        elif nt == 'G':
            G += 1
        elif nt == 'T':
            T += 1
        else:
            N += 1
    print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))


# list variation: create a list to hold the counts

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    counts = [0, 0, 0, 0, 0] # initializing a list, each index being a different nucleotide
    for nt in seq:
        if nt == 'A':
            counts[0] += 1
        elif nt == 'C':
            counts[1] += 1
        elif nt == 'G':
            counts[2] += 1
        elif nt == 'T':
            counts[3] += 1
        else:
            counts[4] += 1
    print(name, end=' ')    # printing the name and formatting
    for n in counts: 
        print(n/len(seq), end=' ')
    print() #needed to start a new line

# indexing with str.find()

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    nts = 'ACGTN'
    counts = [0] * len(nts)
    for nt in seq:
        idx = nts.find(nt) # each nt retrieved from the sequence is compared to the alphabet in nts
        counts[idx] += 1
    print(name, end=' ')   
    for n in counts: 
        print(n/len(seq), end=' ')
    print() 

# counting all letters

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    nts = []
    counts = []
    for nt in seq:
        if nt not in nts: # if the nucleotide is not yet recorded then add it
            nts.append(nt)
            counts.append(0) # set the count to 0
        idx = nts.index(nt)
        counts[idx]+= 1
    print(name) 
    for nt, n in zip(nts, counts): 
        print(nt,n, n/len(seq))
    print() 

'''

# use str.count() to count specific letters

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    print(name, end=' ') 
    for nt in 'ACGTN':
        print(seq.count(nt)/len(seq), end=' ')
    print() 