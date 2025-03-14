import sys
import mcb185


let_code = "IVLFCMAGTSWYPHEQDNKR"

h_score = [
    4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, 
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

'''
def kd(seq):
    total = 0
    for nt in range(len(seq) - 2):
        codon = seq[nt:nt+3]
        if mcb185.translate(codon) in let_code:
            total += h_score[let_code.index(mcb185.translate(codon))]
    return total / len(seq)
'''

kd_dict = dict(zip(let_code, h_score))

def kd(seq):
    total = 0
    aa = mcb185.translate(seq)
    for aa in seq:
        if aa in kd_dict:  
            total += kd_dict[aa]
    return total / len(seq)


x = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):

    signal = False
    trans = False

    n_term = seq[0:30]
    c_term = seq[30:]

    for i in range(0, len(n_term)-8+1, 1):
        if kd(n_term[i:i+8]) >= 2.5:
            signal = True

    for i in range(0, len(c_term)-11+1, 1):
        if kd(c_term[i:i+11]) >= 2.0:
            trans = True 

    if signal == True and trans == True:
        print(defline)
        x += 1

print(x) #521 proteins