import os, sys, csv , operator

sn = 'd:\\data\\eastmoney\\'
dn = 'd:\\data\\emsort\\'
filelist = os.listdir('d:\\data\\eastmoney')

for fn in filelist :
    print('readfile <-- ', fn)
    with open('{}{}'.format(sn,fn), encoding='UTF-8') as fr :
        data = csv.reader(fr, delimiter='|')
        sortedlist = sorted(data, key = lambda x: x[0], reverse=True)

    with open('{}{}'.format(dn,fn), "w", encoding='UTF-8', newline = '') as fw:
        fileWriter = csv.writer(fw, delimiter='|')
        for row in sortedlist :
            fileWriter.writerow(row)

    fw.close()
    fr.close()
    print('writefile --> ', fn)
