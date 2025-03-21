import sys
import mcb185
import itertools

k = int(sys.argv[2])
kcount = {}
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for nt in seq[::-1]:
        rev_seq = ''.join(complement[nt])
    for i in range(len(seq) -k +1):
        kmer = seq[i: i + k]
        if kmer not in kcount:
            kcount[kmer] = 0
        kcount[kmer] += 1
    
    rev_seq = seq[::-1]
    for i in range(len(rev_seq) -k +1):
        r_kmer = rev_seq[i: i + k]
        if r_kmer not in kcount:
            kcount[r_kmer] = 0
        kcount[r_kmer] += 1

#for kmer, n in kcount.items():
    #print(kmer, n)

counter = 0
# generate all possible kmers and check them against the kcount dictionary
for nts in itertools.product('ACGT', repeat = k):
    kmer = ''.join(nts) # joins the tuple nts into a string so we can use it to index our dictionary
    if kmer not in kcount:
        print(kmer, 0)
        counter += 1

print(counter)