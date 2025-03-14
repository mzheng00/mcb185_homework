import sys
import mcb185
import math

in_file = sys.argv[1]
out_file = 'dustoutput.txt'
w = int(sys.argv[2])
et = float(sys.argv[3])

def entropy(seq):
    e = 0.0
    A = seq.count('A')
    G = seq.count('G')
    C = seq.count('C')
    T = seq.count('T')
    for num in [A, G, C, T]:
        if num > 0:
            prob = num / len(seq)
            e -= prob * math.log2(prob)
    return e


with open(out_file, 'w') as outfile:
    for defline, seq in mcb185.read_fasta(sys.argv[1]):
        outfile.write(defline + '\n')
        seq_list = list(seq)
        for i in range(len(seq) - w + 1):
            s = seq[i:i+w]
            if entropy(s) < et:
                for j in range(i, i+w):
                    seq_list[j] = 'N'
        outfile.write(''.join(seq_list)+'\n')


