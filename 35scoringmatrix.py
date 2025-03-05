import sys

sequence = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

def labels(seq):
    label = '   ' + '  '.join(seq)
    return label

def matrix(string, m, mism):
    n = len(string)
    row = []
    for i in range(n):
        row_val = []
        for j in range(n):
            if string[i] == string[j]:
                row_val.append(f'{m}')
            else:
                row_val.append(f'{mism}')
        row.append(f'{string[i]} ' + ' '.join(row_val))
    return '\n'.join(row)


print(labels(sequence))
print(matrix(sequence, match, mismatch))

