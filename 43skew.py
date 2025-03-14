# program uses a sliding window algorithm to compute GC composition and GC-skew along the length of the sequence

import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
   s = seq[i:i+w]
   print(i, sequence.gc_comp(s), sequence.gc_skew(s))