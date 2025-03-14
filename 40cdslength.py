import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':  # skipping over comments
            words = line.split()    # splitting the line into words
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1)    # finding the length of the CDS