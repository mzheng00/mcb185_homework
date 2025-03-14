import sys
import mcb185

in_file = sys.argv[1]
length_aa = int(sys.argv[2])

with open(in_file, 'r') as fp:
    for defline, seq in mcb185.read_fasta(in_file):
        proteins = []
        pos = 0
        for frame in range(3):
            trans_seq = mcb185.translate(seq[frame:])
            for orf in trans_seq.split('*'):
                if 'M' in orf:
                    start = orf.find('M')
                    protein = orf[start:]
                    if len(protein) >= length_aa:
                        proteins.append((f'>{defline[:11]}-prot-{pos}', protein))
                    pos += len(orf) + 1

        rev_seq = seq[::-1]
        rev_seq = rev_seq.translate(str.maketrans('ATCG', 'TAGC'))  # Manually complement the sequence
        for frame in range(3):
            trans_seq2 = mcb185.translate(rev_seq[frame:])
            for orf in trans_seq2.split('*'):
                if 'M' in orf:
                    start = orf.find('M')
                    protein2 = orf[start:]
                    if len(protein2) >= length_aa:
                        proteins.append((f'>{defline[:11]}-prot-{pos}',protein2))
                    pos += len(orf) + 1
        
        for name, protein in proteins:
            print(f'>{name}\n{protein}*\n')