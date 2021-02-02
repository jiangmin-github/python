# Protein to DNA algorithm
import itertools
import random
import math

ProStr = {'F': 0, 'L': 1, 'I': 2, 'M': 3, 'V': 4, 'S': 5, 'P': 6, 'T': 7, 'A': 8, 'Y': 9, 'H': 10, 'Q': 11,
          'N': 12, 'K': 13, 'D': 14, 'E': 15, 'C': 16, 'W': 17, 'R': 18, 'G': 19}
DNAStr = [["TTT", "TTC"], ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"], ["ATT", "ATC", "ATA"], ["ATG"],
          ["GTT", "GTC", "GTA", "GTG"], ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
          ["CCT", "CCC", "CCA", "CCG"], ["ACT", "ACC", "ACA", "ACG"], ["GCT", "GCC", "GCA", "GCG"],
          ["TAT", "TAC"], ["CAT", "CAC"], ["CAA", "CAG"], ["AAT", "AAC"], ["AAA", "AAG"], ["GAT", "GAC"],
          ["GAA", "GAG"], ["TGT", "TGC"], ["TGG"], ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
          ["GGT", "GGC", "GGA", "GGG"]]
mystr = ["GGGGSGGGGSSGRGG",
         "LGGQGAGAAAAAGGA",
         "GQGGYGGLGSQGTSG",
         "RGGLGGQGAGAAAAA",
         "GGAGQGGYGGLGSQG",
         "TSGRGGLGGQGAGAA",
         "AAAGGAGQGGYGGLG",
         "SQGTSGRGGLGGQGA",
         "GAAAAAGGAGQGGYG",
         "GLGSQGTSGRGGLGG",
         "QGAGAAAAAGGAGQG",
         "GYGGLGSQGTSGRGG",
         "LGGQGAGAAAAAGGA",
         "GQGGYGGLGSQGTGG"]

DNAIdx = []
DNAResult = []
DNAperm = []
DNATrace = []
DNAfact = []

mylen = len(mystr)
dnalen = len(DNAStr)

for j in range(mylen):
    DNAResult.append([])

for k in range(dnalen):
    DNAIdx.append([0, 0])
    DNAfact.append(math.factorial(len(DNAStr[k])))
    DNAIdx[k][0] = random.randint(0, DNAfact[k]-1)
    DNAperm.append(list(itertools.permutations(DNAStr[k], len(DNAStr[k]))))
    DNATrace.append([DNAIdx[k][0]])

for i in range(mylen):
    for ProCha in mystr[i]:
        idx = ProStr[ProCha]

        if DNAIdx[idx][1] >= len(DNAStr[idx]):
            oldidx = DNAIdx[idx][0]
            oldDNA = DNAperm[idx][DNAIdx[idx][0]][DNAIdx[idx][1]-1]
            DNAIdx[idx][0] = random.randint(0, DNAfact[idx]-1)
            DNAIdx[idx][1] = 0

            if len(DNAStr[idx]) >= 3:
                while oldidx == DNAIdx[idx][0]:
                    DNAIdx[idx][0] = random.randint(0, DNAfact[idx]-1)
                if oldDNA == DNAperm[idx][DNAIdx[idx][0]][DNAIdx[idx][1]]:
                    DNAIdx[idx][1] += 1
            DNATrace[idx].append(DNAIdx[idx][0])

        DNAResult[i].append(DNAperm[idx][DNAIdx[idx][0]][DNAIdx[idx][1]])
        DNAIdx[idx][1] += 1

print("The trace is :")
for i in range(dnalen):
    for j in range(len(DNATrace[i])):
        print(DNATrace[i][j], end=" ")
    print()
print()

print("The Result is :")
for i in range(mylen):
    for j in range(len(DNAResult[i])):
        print(DNAResult[i][j], end=" ")
    print()

exit(0)
