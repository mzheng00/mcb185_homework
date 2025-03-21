import sys
import mcb185

in_file = sys.argv[1]
length_orf = int(sys.argv[2])
stop_codons = ['TAA', 'TAG', 'TGA']

with open(in_file, 'r') as fp:
    for defline, seq in mcb185.read_fasta(in_file):
        for frame in range(3):
            i = frame
            while i < len(seq) - 2:
                codon = seq[i:i+3]
                if codon == 'ATG':
                    for j in range(i+3, len(seq)-2, 3):
                        stop = seq[j:j+3]
                        if stop in stop_codons:
                            orf = seq[i:j+3]
                            if len(orf) >= length_orf:
                                print(f'{defline[:11]} CDS at {i+1} {j+3} with a length of {len(orf)}')
                            i = j + 3
                            break
                    else:
                        i += 3
                else:
                    i += 3

        rev_seq = seq[::-1]
        for frame in range(3):
            i = frame
            while i < len(rev_seq) - 2:
                codon = rev_seq[i:i+3]
                if codon == 'ATG':
                    for j in range(i+3, len(rev_seq)-2, 3):
                        stop = rev_seq[j:j+3]
                        if stop in stop_codons:
                            orf = rev_seq[i:j+3]
                            if len(orf) >= length_orf:
                                print(f'{defline[:11]} CDS on minus strand from {len(seq) - (j + 3) + 1} to {len(seq) - i} length {len(orf)}')
                            i = j + 3
                            break
                    else:
                        i += 3
                else:
                    i += 3
    