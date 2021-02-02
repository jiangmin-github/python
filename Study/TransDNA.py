# Protein to DNA algorithm

ProStr = {'F':[0,0,0], 'L':[1,0,0], 'I':[2,0,0], 'M':[3,0,0], 'V':[4,0,0], 'S':[5,0,0], 'P':[6,0,0],
          'T':[7,0,0], 'A':[8,0,0], 'Y':[9,0,0], 'H':[10,0,0], 'Q':[11,0,0], 'N':[12,0,0], 
          'K':[13,0,0], 'D':[14,0,0], 'E':[15,0,0], 'C':[16,0,0], 'W':[17,0,0], 'R':[18,0,0],
          'S':[19,0,0], 'G':[20,0,0]}
DNAStr = [["TTT","TTC"], ["TTA","TTG","CTT","CTC","CTA","CTG"], ["ATT","ATC","ATA"], ["ATG"], 
          ["GTT","GTC","GTA","GTG"], ["TCT","TCC","TCA","TCG"], ["CCT","CCC","CCA","CCG"],
          ["ACT","ACC","ACA","ACG"], ["GCT","GCC","GCA","GCG"], ["TAT","TAC"], ["CAT","CAC"],
          ["CAA","CAG"], ["AAT","AAC"], ["AAA","AAG"], ["GAT","GAC"], ["GAA","GAG"], ["TGT","TGC"],
          ["TGG"], ["CGT","CGC","CGA","CGG","AGA","AGG"], ["AGT","AGC"], ["GGT","GGC","GGA","GGG"]]
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
         "GQGGYGGLGSQGT  "]

DNACheck = []

for i in range(DNAStr):
	DNACheck.append("ABC")
print(DNACheck)