# Protein to DNA algorithm
import itertools
import random

ProStr = {'F':0, 'L':1, 'I':2, 'M':3, 'V':4, 'S':5, 'P':6, 'T':7, 'A':8, 'Y':9, 'H':10, 'Q':11,
          'N':12,'K':13,'D':14,'E':15,'C':16,'W':17,'R':18,'G':19}
DNAStr = [["TTT","TTC"], ["TTA","TTG","CTT","CTC","CTA","CTG"], ["ATT","ATC","ATA"], ["ATG"], 
          ["GTT","GTC","GTA","GTG"], ["TCT","TCC","TCA","TCG","AGT","AGC"], ["CCT","CCC","CCA","CCG"],
          ["ACT","ACC","ACA","ACG"], ["GCT","GCC","GCA","GCG"], ["TAT","TAC"], ["CAT","CAC"],
          ["CAA","CAG"], ["AAT","AAC"], ["AAA","AAG"], ["GAT","GAC"], ["GAA","GAG"], ["TGT","TGC"],
          ["TGG"], ["CGT","CGC","CGA","CGG","AGA","AGG"], ["GGT","GGC","GGA","GGG"]]
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
DNACheck = []
DNATrace = []

for j in range(14):
  DNAResult.append([])

for k in range(20):
  DNAIdx.append([0,0])
  DNAIdx[k][0] = random.randint(0,len(DNAStr[k])-1)
  DNATrace.append([DNAIdx[k][0]])

  # print(DNAStr[k])
  # print(len(DNAStr[k]))
  DNACheck.append(list(itertools.permutations(DNAStr[k],len(DNAStr[k]))))
  # if k == 19:
  #  print(DNACheck[k])

# print(DNAIdx)

for i in range(14):
  for ProCha in mystr[i]:
    #print("---------------------------")
    #print(ProCha)
    #print(ProStr[ProCha])
    #print(DNAStr[ProStr[ProCha]])
    #print(len(DNAStr[ProStr[ProCha]]))

    idx = ProStr[ProCha]

    #print(DNAIdx[idx][1])
    '''
    if idx == 1 :
      print("-----")
      print(DNAIdx[idx][1])
      print(len(DNAStr[idx]))
      print("******")
    '''
      
    if DNAIdx[idx][1] >= len(DNAStr[idx]):
      oldidx = DNAIdx[idx][0]
      oldDNA = DNACheck[idx][DNAIdx[idx][0]][DNAIdx[idx][1]-1]
      DNAIdx[idx][0] = random.randint(0,len(DNAStr[idx])-1)
      DNAIdx[idx][1] = 0
      if len(DNAStr[idx]) >= 3 :
        while oldidx == DNAIdx[idx][0] :
          DNAIdx[idx][0] = random.randint(0,len(DNAStr[idx])-1)
        if oldDNA == DNACheck[idx][DNAIdx[idx][0]][DNAIdx[idx][1]] :
          DNAIdx[idx][1] += 1
      DNATrace[idx].append(DNAIdx[idx][0])

    #print(DNAIdx[idx][0])
    #print(DNAIdx[idx][1])
    # print(DNACheck[idx])
    DNAResult[i].append(DNACheck[idx][DNAIdx[idx][0]][DNAIdx[idx][1]])
    DNAIdx[idx][1] += 1
  
  #print(DNAResult[i])

print("The Result is :")
for i in range(20):
  for j in range(len(DNATrace[i])) :
    print(DNATrace[i][j],end=" ")
  print()
print()

for i in range(14):
  for j in range(len(DNAResult[i])):
    print(DNAResult[i][j],end=" ")
  print()